import requests
from elasticsearch import Elasticsearch
from datetime import datetime
from bs4 import BeautifulSoup
from multiprocessing import Process
from pytz import timezone
from time import sleep
import random
import re
from crawler.morpheme.morpheme import Morpheme

class NewsCrawler:
    es = Elasticsearch()
    mor = Morpheme()
    newsUrl=""
    exceptUrl=[]

    def __init__(self):
        self.newsUrl = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001"
        #속보 : https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001
        #정치 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100
        #경제 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101
        #사회 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=102
        #생활 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=103
        #세계 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=104
        #과학 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105
        self.exceptUrl = ['oid=091', #해외뉴스
                          'oid=077', #해외뉴스
                          'oid=410', #mkSports
                          'oid=076', #sports조선
                          'oid=382', #스포츠동아
                          'oid=396', #스포츠월드
                          'oid=144', #스포츠경향
                          'oid=413', #인터풋볼
                          'oid=351', #바스켓코리아
                          'oid=065', #점프볼
                          'oid=477', #스포츠티비
                          'oid=358', #스포탈
                          'oid=468', #스포츠서울
                          ]

    def crawling(self,_page):
        newsLinks = []

        for i in range(1,11):
            url = str(self.newsUrl) + "&page=" + str(_page+i)
            request = requests.get(url);
            html = request.text
            htmlSoup = BeautifulSoup(html, 'html.parser')
            onePageNewsLinks=htmlSoup.select(
                '#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt:nth-child(1) > a'
            )

            for link in onePageNewsLinks:
                newsLinks.append(link['href'])


        for link in newsLinks :
            print(link)
            newsDetailUrl = link

            oid = str(newsDetailUrl.split('oid=')[1].split('&')[0])
            aid = str(newsDetailUrl.split('aid=')[1].split('&')[0])

            newsId = oid+aid #뉴스 아이디 지정


            #제외 언론사
            if  "oid=091" in newsDetailUrl or \
                "oid=077" in newsDetailUrl or \
                "oid=410" in newsDetailUrl or \
                "oid=076" in newsDetailUrl or \
                "oid=382" in newsDetailUrl or \
                "oid=396" in newsDetailUrl or \
                "oid=144" in newsDetailUrl or \
                "oid=413" in newsDetailUrl or \
                "oid=351" in newsDetailUrl or \
                "oid=065" in newsDetailUrl or \
                "oid=477" in newsDetailUrl or \
                "oid=358" in newsDetailUrl or \
                "oid=468" in newsDetailUrl :
                continue;

            request = requests.get(newsDetailUrl)

            html = request.text
            htmlSoup = BeautifulSoup(html, 'html.parser')

            newsDate = htmlSoup.select('#main_content > div.article_header > div.article_info > div > .t11')
            newsDate = datetime.strptime(newsDate[0].text,"%Y-%m-%d %H:%M")
            conNewsDate = datetime.strftime(newsDate,"%Y-%m-%d")

            try : # 중복기사 크롤링 막기
                if self.es.get(index = 'news-'+conNewsDate, doc_type = 'break', id = newsId) != None :
                    print('duplication news')
                    break
            except :
                print('new news')

            newsProfile = htmlSoup.select('#articleBodyContents > span.end_photo_org > img')
            if len(newsProfile)>0 :
                newsProfile = newsProfile[0]['src']
            else :
                newsProfile = None


            newsTitle = htmlSoup.select('#articleTitle')[0].text
            newsContents = str(htmlSoup.select('#articleBodyContents'))

            newsContents = re.sub('<script.*?>.*?</script>', '', newsContents, 0, re.I|re.S)
            newsContents = re.sub('<a.*?>.*?</a>', '', newsContents, 0, re.I|re.S)
            newsContents = re.sub('<.+?>', '', newsContents, 0, re.I|re.S)

            self.mor.store(newsTitle,newsContents)
            self.mor.keyword()
            self.mor.company_check()
            if self.mor.positive()!=0 and len(self.mor.companies)!=0 :

                news = {
                    'profile': newsProfile,
                    'title': newsTitle,
                    'contents': newsContents,
                    'keyword': self.mor.keywords,
                    'positive': self.mor.positiveScore,
                    'company': self.mor.companies,
                    'date':  newsDate,
                    'crawling_date': datetime.strftime(datetime.now(timezone('Asia/Seoul')),"%Y-%m-%d %H:%M"),
                    'url': newsDetailUrl,
                }
                response = self.es.index(index='news-'+conNewsDate, doc_type='break', body=news, id=newsId)
                print(response)


    def search(self):

        query = {
            "sort": [
                {"date": {"order": "desc"}},
            ],
            "query": {
                "term": {"contents": "네이버"}
                }
            }

        res = self.es.search(index="news", body=query)

        return res


    def start(self):
        for i in range(0,20):
            proc = Process(target=self.crawling, args=(10*i,))
            proc.start()

    def initial_start(self):

        for k in range(1,13):
            strk = str(k)
            if k<10:
                strk = '0'+strk

            for j in range(1,29):
                strj = str(j)
                if j<10:
                    strj = '0'+strj;


                # self.newsUrl = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=2017"+strk+strj
                 # self.crawling(10)
                for i in range(3,14):
                    proc = Process(target=self.crawling, args=(10*i,))
                    proc.start()
                    sleep(0.5)

        sleep(10)
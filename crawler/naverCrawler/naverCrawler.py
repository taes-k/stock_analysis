import requests
from elasticsearch import Elasticsearch
from datetime import datetime
from bs4 import BeautifulSoup
from multiprocessing import Process
from pytz import timezone
from time import sleep
import re
from crawler.morpheme.morpheme import Morpheme

class NewsCrawler:
    es = Elasticsearch()
    #es = Elasticsearch(host='45.119.146.58',port='9200')
    mor = Morpheme()
    news_url=''
    exceptUrl=[]

    def __init__(self):
        self.news_url = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001'
        self.except_url_list = ['oid=091', #해외뉴스
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
        news_link_list = []

        for i in range(1,11):
            url = str(self.news_url) + "&page=" + str(_page+i)
            request = requests.get(url);
            html = request.text
            soup = BeautifulSoup(html, 'html.parser')
            news_links=soup.select(
                '#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt:nth-child(1) > a'
            )

            for link in news_links:
                news_link_list.append(link['href'])


        for link in news_link_list :
            print('link : ' + link)
            url = link

            oid = str(url.split('oid=')[1].split('&')[0])
            aid = str(url.split('aid=')[1].split('&')[0])

            news_id = oid+aid #뉴스 아이디 지정

            except_check = False
            #제외 언론사 필터링
            for except_url in self.except_url_list:
                if except_url in url:
                    except_check = True
                    break

            if except_check :
                continue
            #제외 언론사 필터링

            request = requests.get(url)

            html = request.text
            soup = BeautifulSoup(html, 'html.parser')

            news_date = soup.select('#main_content > div.article_header > div.article_info > div > .t11')
            news_date = datetime.strptime(news_date[0].text.replace(u'오전','AM').replace(u'오후','PM'),"%Y.%m.%d. %p %I:%M")
            convert_news_date = datetime.strftime(news_date,"%Y-%m-%d")

            try : # 중복기사 크롤링 막기
                #Duplication news
                if self.es.get(index = 'news-'+convert_news_date, doc_type = 'break', id = news_id) != None :
                    print('duplication news')
                    break
            except :
                #New news
                print('new news')

            news_profile = soup.select('#articleBodyContents > span.end_photo_org > img')
            if len(news_profile)>0 :
                news_profile = news_profile[0]['src']
            else :
                news_profile = None


            news_title = soup.select('#articleTitle')[0].text
            news_contents = str(soup.select('#articleBodyContents'))

            #태그제거
            news_contents = re.sub('<script.*?>.*?</script>', '', news_contents, 0, re.I|re.S)
            news_contents = re.sub('<a.*?>.*?</a>', '', news_contents, 0, re.I|re.S)
            news_contents = re.sub('<.+?>', '', news_contents, 0, re.I|re.S)
            news_contents = re.sub('&lt.*?&gt', '', news_contents, 0, re.I|re.S)
            news_contents = re.sub('저작권자.*?금지', '', news_contents, 0, re.I|re.S)
            news_contents = re.sub('무단전재.*?금지', '', news_contents, 0, re.I|re.S)

            self.mor.store(news_title,news_contents)

            positive_score = self.mor.get_positive()
            keyword_list = self.mor.get_keyword()
            related_company_list = self.mor.get_company()


            if abs(positive_score)==1 and len(related_company_list)!=0 :

                news = {
                    'profile': news_profile,
                    'title': news_title,
                    'contents': news_contents,
                    'keyword': keyword_list,
                    'positive': positive_score,
                    'company': related_company_list,
                    'crawling_date': datetime.strftime(datetime.now(timezone('Asia/Seoul')),"%Y-%m-%d %H:%M:%S"),
                    'date':  datetime.strftime(news_date,"%Y-%m-%d %H:%M:%S"),
                    'url': url,
                }
                response = self.es.index(index='news', doc_type='news_type', body=news, id=news_id)

    def search(self,text):
        query = {
            "sort": [
                {"date": {"order": "desc"}},
            ],
            "query": {
                "term": {"contents": text}
                }
            }

        result = self.es.search(index="news", body=query)

        return result


    def crawling_start(self):
        for i in range(0,4):
            self.crawling(10*i)
            # proc = Process(target=self.crawling, args=(10*i,))
            # proc.start()

    def initial_crawling_start(self):
        for month in range(1,6):
            str_month = str(month)
            if month<10:
                str_month = '0'+str_month
            for day in range(1,29):
                str_day = str(day)
                if day<10:
                    str_day = '0'+str_day;
                self.newsUrl = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=2019"+str_month+str_day
                for page in range(3,14):
                    proc = Process(target=self.crawling, args=(10*page,))
                    proc.start()
                    sleep(0.5)
            sleep(10)

    # 자동 크롤링을 위한 api (5분에 10개의 기사를 스크랩을 기준으로 함)
    def auto_crawling_start(self):
        self.crawling(0);
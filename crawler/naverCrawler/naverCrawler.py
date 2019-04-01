import requests
from elasticsearch import Elasticsearch
from datetime import datetime
from bs4 import BeautifulSoup
from multiprocessing import Process
from pytz import timezone
import re

class NewsCrawler:
    es = Elasticsearch()

    def __init__(self):
        self.newsUrl = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001"
        #속보 : https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001
        #정치 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100
        #경제 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101
        #사회 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=102
        #생활 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=103
        #세계 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=104
        #과학 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105

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

            if "oid=091" in newsDetailUrl or "oid=077" in newsDetailUrl :
                continue;

            request = requests.get(newsDetailUrl);
            html = request.text
            htmlSoup = BeautifulSoup(html, 'html.parser')

            newsTitle = htmlSoup.select('#articleTitle')
            newsContents = str(htmlSoup.select('#articleBodyContents'))
            newsDate = htmlSoup.select('#main_content > div.article_header > div.article_info > div > .t11')
            newsDate = datetime.strptime(newsDate[0].text,"%Y-%m-%d %H:%M")

            newsContents = re.sub('<.+?>', '', newsContents, 0).strip()


            print(newsContents)
            conNewsDate = datetime.strftime(newsDate,"%Y-%m-%d")
            news = {
                'title': newsTitle[0].text,
                'contents': newsContents[0].text,
                'positive': 0,
                'date': datetime.strftime(newsDate,"%Y-%m-%d %H:%M"),
                'crawling_date': datetime.strftime(datetime.now(timezone('Asia/Seoul')),"%Y-%m-%d %H:%M"),
                'url': newsDetailUrl,
            }
            response = self.es.index(index='news-'+conNewsDate, doc_type='break', body=news)
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
        for i in range(0,2):
            proc = Process(target=self.crawling, args=(10*i,))
            proc.start()
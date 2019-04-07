import requests
from elasticsearch import Elasticsearch
from datetime import datetime
from bs4 import BeautifulSoup
from multiprocessing import Process
from pytz import timezone
import re
from crawler.morpheme.morpheme import Morpheme

class DictionaryInitCrawler:
    mor = Morpheme()
    newsLinks = []

    def __init__(self,newsLinks):
        self.newsLinks = newsLinks

    def positive(self):

        for link in self.newsLinks :
            print(link)
            newsDetailUrl = link

            request = requests.get(newsDetailUrl);
            html = request.text
            htmlSoup = BeautifulSoup(html, 'html.parser')

            newsTitle = htmlSoup.select('#articleTitle')[0].text
            newsContents = str(htmlSoup.select('#articleBodyContents'))
            newsDate = htmlSoup.select('#main_content > div.article_header > div.article_info > div > .t11')
            newsDate = datetime.strptime(newsDate[0].text,"%Y-%m-%d %H:%M")

            newsContents = re.sub('<script.*?>.*?</script>', '', newsContents, 0, re.I|re.S)
            newsContents = re.sub('<a.*?>.*?</a>', '', newsContents, 0, re.I|re.S)
            newsContents = re.sub('<.+?>', '', newsContents, 0, re.I|re.S)

            self.mor.store(newsTitle,newsContents)
            self.mor.positiveinit()


    def negative(self):
        for link in self.newsLinks:
            print(link)
            newsDetailUrl = link

            request = requests.get(newsDetailUrl);
            html = request.text
            htmlSoup = BeautifulSoup(html, 'html.parser')

            newsTitle = htmlSoup.select('#articleTitle')[0].text
            newsContents = str(htmlSoup.select('#articleBodyContents'))
            newsDate = htmlSoup.select('#main_content > div.article_header > div.article_info > div > .t11')
            newsDate = datetime.strptime(newsDate[0].text, "%Y-%m-%d %H:%M")

            newsContents = re.sub('<script.*?>.*?</script>', '', newsContents, 0, re.I | re.S)
            newsContents = re.sub('<a.*?>.*?</a>', '', newsContents, 0, re.I | re.S)
            newsContents = re.sub('<.+?>', '', newsContents, 0, re.I | re.S)

            self.mor.store(newsTitle, newsContents)
            self.mor.negativeinit()

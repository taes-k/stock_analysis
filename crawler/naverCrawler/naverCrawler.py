import requests
from bs4 import BeautifulSoup

class NewsCrawler:
    def __init__(self):
        self.newsUrl = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001"
        #속보 : https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001
        #정치 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100
        #경제 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101
        #사회 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=102
        #생활 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=103
        #세계 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=104
        #과학 : https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105

    def crawling(self,_date,_page):
        url = str(self.newsUrl)+"&date="+str(_date)+"&page="+str(_page)
        request = requests.get(url);
        html = request.text
        htmlSoup = BeautifulSoup(html, 'html.parser')

        newsTitle = htmlSoup.select(
            '#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt > a'
        )

        for title in newsTitle :
            print(title.text)
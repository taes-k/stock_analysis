from django.shortcuts import render
from crawler.naverCrawler.naverCrawler import NewsCrawler
from crawler.naverCrawler.dictionaryInitCrawler import DictionaryInitCrawler

# Create your views here.
def index(request):
    crawler = NewsCrawler()
    result = crawler.start()

def search(request):
    crawler = NewsCrawler()
    crawler.search()
    # return HttpResponse ("Hello, World!")


def positiveInit(request):
    positiveList = ['https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=011&aid=0003534247',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=014&aid=0004206803',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=119&aid=0002321523',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=092&aid=0002159467',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=029&aid=0002519089',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=005&aid=0001188149',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=030&aid=0002799431',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=018&aid=0004348001',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=109&aid=0003984797',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=277&aid=0004444676',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=003&aid=0009158853',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=092&aid=0002159477',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=421&aid=0003924140',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=029&aid=0002519069',]
    negativeList = ['https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=022&aid=0003352781',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=366&aid=0000431096',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=366&aid=0000431099',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=082&aid=0000893036',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=421&aid=0003924356',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=022&aid=0003352781',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=002&aid=0002087092',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=052&aid=0001276478',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=214&aid=0000938587',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=052&aid=0001276423',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=015&aid=0004120496',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=421&aid=0003924150',
                    'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=366&aid=0000430924']
    crawler = DictionaryInitCrawler(positiveList)
    crawler.positive()
    crawler2 = DictionaryInitCrawler(negativeList)
    crawler2.negative()

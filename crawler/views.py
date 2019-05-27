from django.shortcuts import render
from crawler.naverCrawler.naverCrawler import NewsCrawler

# Create your views here.
def crawling(request):
    crawler = NewsCrawler()
    result = crawler.crawling_start()

def search(request):
    crawler = NewsCrawler()
    crawler.search()
    # return HttpResponse ("Hello, World!")

def initCrawling(request):
    crawler = NewsCrawler()
    result = crawler.initial_crawling_start()

def autoCrawling(request):
    crawler = NewsCrawler()
    result = crawler.auto_crawling_start()

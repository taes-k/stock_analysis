from django.shortcuts import render
from crawler.naverCrawler.naverCrawler import NewsCrawler

# Create your views here.
def index(request):
    crawler = NewsCrawler()
    result = crawler.crawling_start()

def search(request):
    crawler = NewsCrawler()
    crawler.search()
    # return HttpResponse ("Hello, World!")

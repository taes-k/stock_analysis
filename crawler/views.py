from django.shortcuts import render
from crawler.naverCrawler.naverCrawler import NewsCrawler

# Create your views here.
def index(request):
    crawler = NewsCrawler()
    crawler.start()
    return render(request, "index.html")
    # return HttpResponse ("Hello, World!")
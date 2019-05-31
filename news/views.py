from news.module.news import News
from django.http import HttpResponse, JsonResponse

# Create your views here.
def getNews(request):
    news = News()
    result = JsonResponse(news.getNews(0))
    return result

def searchNews(request):
    news = News()
    result = JsonResponse(news.searchNews(request.GET['text']))
    return result

def getUpdateNews(request):
    news = News()
    result = JsonResponse(news.getUpdateNews(request.GET['crawlingDate']))
    return result

def getPreviousNews(request):
    news = News()
    result = JsonResponse(news.getPreviousNews(request.GET['crawlingDate']))
    return result





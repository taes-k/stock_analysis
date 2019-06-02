from elasticsearch import Elasticsearch
import json

class News:
    es = Elasticsearch()
    #es = Elasticsearch(host='45.119.146.58',port='9200')
    def __init__(self):
        print("news init")

    def getNews(self,_page):

        result = {}
        res = self.es.search(index="news", sort='crawling_date:desc', size='9')
        res = ((res['hits'])['hits'])
        result['res'] = res
        print(result)

        return result

    def searchNews(self,_text):

        result = {}
        query = {
            "query": {
                "term": {"keyword": _text}
                }
            }
        res = self.es.search(index="news", sort='date:desc', body=query)

        res = ((res['hits'])['hits'])
        result['res'] = res

        return result

    def getUpdateNews(self,_crawlingDate):

        result = {}
        query = {
                    "query": {
                        "range": {
                            "crawling_date": {
                                "gte": _crawlingDate
                            }
                        }
                    },
                    "sort": [
                        {"crawling_date": "asc"}
                    ]
                }


        print("HEELELEOO :::: ",_crawlingDate )

        res = self.es.search(index="news", body=query, size='9')

        res = ((res['hits'])['hits'])
        result['res'] = res

        return result

    def getPreviousNews(self,_crawlingDate):

        result = {}

        query = {
                    "query": {
                        "range": {
                            "crawling_date": {
                                "lte": _crawlingDate
                            }
                        }
                    },
                    "sort": [
                        {"crawling_date": "desc"}
                    ]
                }
        res = self.es.search(index="news", body=query, size='9')

        res = ((res['hits'])['hits'])
        result['res'] = res

        return result
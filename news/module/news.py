from elasticsearch import Elasticsearch
import json

class News:
    es = Elasticsearch()

    def __init__(self):
        print("news init")

    def getNews(self,_page):

        result = {}
        res = self.es.search(index="", sort='date:desc', size='9')
        res = ((res['hits'])['hits'])
        result['res'] = res
        print(result)

        return result

    def searchNews(self,_text):

        result = {}
        query = {
            "query": {
                "term": {"contents": _text}
                }
            }
        res = self.es.search(index="", sort='date:desc', body=query)

        res = ((res['hits'])['hits'])
        result['res'] = res

        return result
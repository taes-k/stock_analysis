from konlpy.tag import Kkma
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient

class Morpheme:
    es = Elasticsearch()
    targetText = ""
    posText = []

    def __init__(self):
        print("init")

    def store(self,text):
        self.targetText=text
        posSetting = {
            "tokenizer": "nori_tokenizer",
            "text": self.targetText,
            "attributes": ["posType", "leftPOS", "rightPOS", "morphemes", "reading"],
            "explain": "true"
        }
        i = IndicesClient(self.es)
        self.posText = i.analyze(index="", body=posSetting)
        print(self.posText)


    def keyword(self):
        keywordDic = {}
        for morpheme in self.posText :
            if keywordDic[morpheme] == "" :
                keywordDic[morpheme]=0
            else :
                keywordDic[morpheme]=keywordDic[morpheme]+1

        sorted(keywordDic, key=lambda k: keywordDic[k], reverse=True)
        keywords = list(keywordDic.keys())
        return keywords[0]


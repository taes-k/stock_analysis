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
        tempText= i.analyze(index="", body=posSetting)
        self.posText = tempText.get('detail').get('tokenizer').get('tokens')

        self.keyword();

    def keyword(self):
        keywordDic = {}
        for morpheme in self.posText :
            print(morpheme.get('leftPOS'))
            if 'NNG' in morpheme.get('leftPOS') or 'NNP' in morpheme.get('leftPOS') or 'NP' in morpheme.get('leftPOS') :
                print(morpheme.get('token'))
                if keywordDic.get(morpheme.get('token')) == None :
                    keywordDic[morpheme.get('token')]=0
                else :
                    keywordDic[morpheme.get('token')]=keywordDic[morpheme.get('token')]+1

        keywords =sorted(keywordDic.items(),key=lambda x: x[1], reverse=True)
        print(str(keywords))
        return keywords[0][0]


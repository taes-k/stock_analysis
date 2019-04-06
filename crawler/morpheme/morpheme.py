from konlpy.tag import Kkma
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
import csv

class Morpheme:
    es = Elasticsearch()
    targetTitle = ""
    targetText = ""
    posTitle = []
    posText = []
    positiveDictionary = {}
    positiveScore = 0

    def __init__(self):
        print("init")
        self.posdic()

    def posdic(self):
        with open('./positiveDictionary.csv', 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if self.positiveDictionary.get(row.get('token')) == None:
                    self.positiveDictionary[(row.get('token'))] = 0.5*row.get('positive')
                else:
                    self.positiveDictionary[(row.get('token'))] = (self.positiveDictionary.get(row.get('token'))+row.get('positive'))/2

    def positive(self):
        for morpheme in self.posText:
            if self.positiveDictionary[(morpheme.get('token')+morpheme.get('leftPOS'))] != None :
                self.positiveScore += self.positiveDictionary[(morpheme.get('token')+morpheme.get('leftPOS'))]

        if self.positiveScore > 0 :
            with open('./positiveDictionary.csv', 'a') as csvfile:
                fieldnames = ['token', 'positive']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for morpheme in self.posText:
                    data = {(morpheme.get('token')+morpheme.get('leftPOS')),1}
                    writer.writerow(data)
        elif self.positiveScore < 0 :
            with open('./positiveDictionary.csv', 'a') as csvfile:
                fieldnames = ['token', 'positive']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for morpheme in self.posText:
                    data = {(morpheme.get('token')+morpheme.get('leftPOS')),-1}
                    writer.writerow(data)

        return self.positiveScore

    def store(self,title,text):
        self.targetTitle = title
        self.targetText = text
        self.positiveScore = 0

        posTitleSetting = {
            "tokenizer": "nori_tokenizer",
            "text": self.targetTitle,
            "attributes": ["posType", "leftPOS", "rightPOS", "morphemes", "reading"],
            "explain": "true"
        }
        posTextSetting = {
            "tokenizer": "nori_tokenizer",
            "text": self.targetText,
            "attributes": ["posType", "leftPOS", "rightPOS", "morphemes", "reading"],
            "explain": "true"
        }
        i = IndicesClient(self.es)
        tempTitle= i.analyze(index="", body=posTitleSetting)
        self.posTitle = tempTitle.get('detail').get('tokenizer').get('tokens')
        tempText= i.analyze(index="", body=posTextSetting)
        self.posText = tempText.get('detail').get('tokenizer').get('tokens')

    def keyword(self):
        keywordDic = {}

        for morpheme in self.posTitle :
            if 'NNG' in morpheme.get('leftPOS') or 'NNP' in morpheme.get('leftPOS') or 'NP' in morpheme.get('leftPOS') :
                if keywordDic.get(morpheme.get('token')) == None :
                    keywordDic[morpheme.get('token')]=5
                else :
                    keywordDic[morpheme.get('token')]=keywordDic[morpheme.get('token')]+5


        for morpheme in self.posText :
            if 'NNG' in morpheme.get('leftPOS') or 'NNP' in morpheme.get('leftPOS') or 'NP' in morpheme.get('leftPOS') :
                if keywordDic.get(morpheme.get('token')) == None :
                    keywordDic[morpheme.get('token')]=1
                else :
                    keywordDic[morpheme.get('token')]=keywordDic[morpheme.get('token')]+1

        keywords =sorted(keywordDic.items(),key=lambda x: x[1], reverse=True)

        keywordsResult = []
        for i in range(0,3) :
            keywordsResult.append(keywords[i][0])

        print(str(keywordsResult))

        return keywordsResult


    def positive(self):
        score = 0

        for morpheme in self.posTitle:
            if 'NNG' in morpheme.get('leftPOS') or 'NNP' in morpheme.get('leftPOS') or 'NP' in morpheme.get('leftPOS'):
                if keywordDic.get(morpheme.get('token')) == None:
                    keywordDic[morpheme.get('token')] = 5
                else:
                    keywordDic[morpheme.get('token')] = keywordDic[morpheme.get('token')] + 5

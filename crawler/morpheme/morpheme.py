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
        with open('./crawler/morpheme/positiveDictionary.csv', 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if self.positiveDictionary.get(row.get('token')) == None:
                    if 'NNG' in row.get('token') or 'XR' in row.get('token') or 'VV' in row.get('token') or 'VA' in row.get('token') or 'VP' in row.get('token') :
                        self.positiveDictionary[(row.get('token'))] = float(row.get('positive'))/2
                else:
                    self.positiveDictionary[(row.get('token'))] = float(self.positiveDictionary.get(row.get('token'))+float(row.get('positive'))/2)/1.8


    def positive(self):
        self.positiveScore = 0
        posiCount = 0
        negaCount = 0
        for morpheme in self.posTitle:
            if self.positiveDictionary.get(str(morpheme.get('token')+morpheme.get('leftPOS'))) != None :
                self.positiveScore += self.positiveDictionary[(morpheme.get('token')+morpheme.get('leftPOS'))]
                if self.positiveDictionary[(morpheme.get('token')+morpheme.get('leftPOS'))] > 0 :
                    posiCount += 1
                else :
                    negaCount += 1

        posiPercent = float(posiCount/len(self.posTitle))
        negaPercent = float(negaCount/len(self.posTitle))

        print(self.targetTitle)
        print(self.positiveScore)
        print("positive Percent : "+str(posiPercent))
        print("negative Percent : "+str(negaPercent))
        # a = input("check : ")
        # if a == '1' :
        #     with open('./crawler/morpheme/positiveDictionary.csv', 'a') as csvfile:
        #         fieldnames = ['token', 'positive']
        #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #         for morpheme in self.posTitle:
        #             data = {'token':(morpheme.get('token')+morpheme.get('leftPOS')),'positive':1}
        #             writer.writerow(data)
        # elif a == '2' :
        #     with open('./crawler/morpheme/positiveDictionary.csv', 'a') as csvfile:
        #         fieldnames = ['token', 'positive']
        #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #         for morpheme in self.posTitle:
        #             data = {'token':(morpheme.get('token')+morpheme.get('leftPOS')),'positive':-1}
        #             writer.writerow(data)

        if self.positiveScore > 0 :
            if posiPercent > 0.3 :
                with open('./crawler/morpheme/positiveDictionary.csv', 'a') as csvfile:
                    fieldnames = ['token', 'positive']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    for morpheme in self.posTitle:
                        data = {'token':(morpheme.get('token')+morpheme.get('leftPOS')),'positive':1}
                        writer.writerow(data)
                        if self.positiveDictionary.get(morpheme.get('token')) == None:
                            if 'NNG' in morpheme.get('token') or 'XR' in morpheme.get('token') or 'VV' in morpheme.get(
                                    'token') or 'VA' in morpheme.get('token') or 'VP' in morpheme.get('token'):
                                self.positiveDictionary[(morpheme.get('token'))] = float(1) / 2
                        else:
                            self.positiveDictionary[(morpheme.get('token'))] = float(
                                self.positiveDictionary.get(morpheme.get('token')) + float(1) / 2) / 1.8


            else :
                self.positiveScore = 0

        elif self.positiveScore < 0 :
            if negaPercent > 0.3 :
                with open('./crawler/morpheme/positiveDictionary.csv', 'a') as csvfile:
                    fieldnames = ['token', 'positive']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    for morpheme in self.posTitle:
                        data = {'token':(morpheme.get('token')+morpheme.get('leftPOS')),'positive':-1}
                        writer.writerow(data)
                        if self.positiveDictionary.get(morpheme.get('token')) == None:
                            if 'NNG' in morpheme.get('token') or 'XR' in morpheme.get('token') or 'VV' in morpheme.get(
                                    'token') or 'VA' in morpheme.get('token') or 'VP' in morpheme.get('token'):
                                self.positiveDictionary[(morpheme.get('token'))] = float(-1) / 2
                        else:
                            self.positiveDictionary[(morpheme.get('token'))] = float(
                                self.positiveDictionary.get(morpheme.get('token')) + float(-1) / 2) / 1.8

            else :
                self.positiveScore = 0


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
        self.posTitle = list({token['token']: token for token in self.posTitle}.values()) # 중복제거

        tempText= i.analyze(index="", body=posTextSetting)
        self.posText = tempText.get('detail').get('tokenizer').get('tokens')
        self.posText = list({token['token']: token for token in self.posText}.values()) # 중복제거

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
        keyLen = (3 if len(keywords)>=3 else len(keywords))

        for i in range(0,keyLen) :
            keywordsResult.append(keywords[i][0])

        print(str(keywordsResult))

        return keywordsResult


    def positiveinit(self):
        with open('./crawler/morpheme/positiveDictionary.csv', 'a') as csvfile:
            fieldnames = ['token', 'positive']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for morpheme in self.posTitle:
                data = {'token':(morpheme.get('token')+morpheme.get('leftPOS')),'positive':1}
                writer.writerow(data)
                print(morpheme.get('token')+morpheme.get('leftPOS'))


    def negativeinit(self):
        with open('./crawler/morpheme/positiveDictionary.csv', 'a') as csvfile:
            fieldnames = ['token', 'positive']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for morpheme in self.posTitle:
                data = {'token':(morpheme.get('token')+morpheme.get('leftPOS')),'positive':-1}
                writer.writerow(data)
                print(morpheme.get('token')+morpheme.get('leftPOS'))
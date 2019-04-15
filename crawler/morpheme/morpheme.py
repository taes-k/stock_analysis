from konlpy.tag import Kkma
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from crawler.morpheme.positive import Positive
from crawler.morpheme.company import Company
import csv

class Morpheme:
    es = Elasticsearch()
    targetTitle = ""
    targetText = ""
    posTitle = []
    posText = []
    keywords = []
    companies = []
    positiveScore = 0

    ps = Positive()
    com = Company()

    def __init__(self):
        print("init")


    def store(self,title,text):
        self.targetTitle = title
        self.targetText = text

        posTitleSetting = {
            "analyzer": "my_analyzer",
            "text": self.targetTitle,
            "attributes": ["posType", "leftPOS", "rightPOS", "morphemes", "reading"],
            "explain": "true"
        }
        posTextSetting = {
            "analyzer": "my_analyzer",
            "text": self.targetText,
            "attributes": ["posType", "leftPOS", "rightPOS", "morphemes", "reading"],
            "explain": "true"
        }
        i = IndicesClient(self.es)
        tempTitle= i.analyze(index="pos", body=posTitleSetting)
        self.posTitle = tempTitle.get('detail').get('tokenizer').get('tokens')
        self.posTitle = list({token['token']: token for token in self.posTitle}.values()) # 중복제거

        tempText= i.analyze(index="pos", body=posTextSetting)
        self.posText = tempText.get('detail').get('tokenizer').get('tokens')
        self.posText = list({token['token']: token for token in self.posText}.values()) # 중복제거


    def positive(self):
        text = ''
        for morpheme in self.posTitle:
            if 'NNG' in morpheme.get('leftPOS') or \
                'XR' in morpheme.get('leftPOS') or \
                'VV' in morpheme.get('leftPOS') or \
                'VA' in morpheme.get('leftPOS') or \
                'VP' in morpheme.get('token') or \
                'MAG' in morpheme.get('token'):
                if not (morpheme.get('token') in self.company_list):
                    text = text + morpheme.get('token') + (morpheme.get('leftPOS').split('(')[0]) + ' '

        if text != '':
            self.positiveScore = self.ps.get_positive(text)

        return self.positiveScore


    def keyword(self):
        self.keywords=[]
        keywordDic = {}

        for morpheme in self.posTitle :
            if 'SL' in morpheme.get('leftPOS') or 'NNG' in morpheme.get('leftPOS') or 'NNP' in morpheme.get('leftPOS') or 'NP' in morpheme.get('leftPOS') :
                if keywordDic.get(morpheme.get('token')) == None :
                    keywordDic[morpheme.get('token')]=3
                else :
                    keywordDic[morpheme.get('token')]=keywordDic[morpheme.get('token')]+3

        for morpheme in self.posText :
            if 'SL' in morpheme.get('leftPOS') or 'NNG' in morpheme.get('leftPOS') or 'NNP' in morpheme.get('leftPOS') or 'NP' in morpheme.get('leftPOS') :
                if keywordDic.get(morpheme.get('token')) == None :
                    keywordDic[morpheme.get('token')]=1
                else :
                    keywordDic[morpheme.get('token')]=keywordDic[morpheme.get('token')]+1

        keywords =sorted(keywordDic.items(),key=lambda x: x[1], reverse=True)

        keyLen = (5 if len(keywords)>=5 else len(keywords))

        for i in range(0,keyLen) :
            self.keywords.append(keywords[i][0])

        print("keywords : "+str(self.keywords))

        return self.keywords

    def company_check(self):
        self.com.get_realated_companies(self.keywords)

        self.companies = []
        companyKeywords = []
        companyScoreDict = {}

        if  not '야구' in self.keywords and\
            not '축구' in self.keywords and\
            not '배구' in self.keywords and\
            not '별세' in self.keywords and\
            not '부고' in self.keywords :

            for keyword in self.keywords:
                if self.companydictionary.get(keyword) != None:
                    for company in self.companydictionary.get(keyword):
                        if companyScoreDict.get(company.get('name')) != None :
                            companyScoreDict[company.get('name')] = companyScoreDict[company.get('name')]+abs(float(company.get('score')))
                        else :
                            companyScoreDict[company.get('name')] = abs(float(company.get('score')))
                        companyKeywords.append((keyword+company.get('name')))


                if keyword in self.company_list :
                    for idx in range(0,2):
                        if not (self.keywords[idx]+keyword) in companyKeywords :
                            score = (keyword == self.keywords[idx] and 1 or (self.keywords[idx] in self.company_list and 0.5 or 0.3))
                            data = {'keyword': self.keywords[idx], 'company': keyword, 'score': score}
                            with open('./crawler/morpheme/positiveCompanyDic.csv', 'a') as csvfile:
                                fieldnames = ['keyword','company','score']
                                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                                writer.writerow(data)

                            companyKeywords.append((self.keywords[idx]+keyword))
                            companyScoreDict[keyword] = score
                            self.companydictionary[self.keywords[idx]] = [{'name': keyword, 'score': score}]

        companies = sorted(companyScoreDict.items(), key=lambda x: abs(x[1]), reverse=True)
        keyLen = (5 if len(companies) >= 5 else len(companies))

        for i in range(0, keyLen):
            if companies[i][1] >= 0.8 :
                self.companies.append({'name':companies[i][0],'score':companies[i][1]})

        print ('찾은회사 @@@@@@@@@@@@@@@@@@@@@@@@0 : '+str(self.companies))


    def positiveinit(self):

        print(self.targetTitle)
        i = input()

        if i!='3' :
            with open('./crawler/morpheme/positiveTrainData.csv', 'a') as csvfile:
                fieldnames = ['text', 'positive']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                text = ''
                for morpheme in self.posTitle:
                    if 'NNG' in morpheme.get('leftPOS') or \
                        'XR' in morpheme.get('leftPOS') or \
                        'VV' in morpheme.get('leftPOS') or \
                        'VA' in morpheme.get('leftPOS') or \
                        'VP' in morpheme.get('token') or \
                        'MAG' in morpheme.get('token'):
                        if not (morpheme.get('token') in self.company_list):
                            text = text + morpheme.get('token')+(morpheme.get('leftPOS').split('(')[0])+' '

                if text!='' :
                    data = {'text': text, 'positive': i }
                    print("저장 Positive 데이터 : "+text)
                    writer.writerow(data)

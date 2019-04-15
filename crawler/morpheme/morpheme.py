from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from crawler.morpheme.positive import Positive
from crawler.morpheme.keyword import Keyword
from crawler.morpheme.company import Company

class Morpheme:
    es = Elasticsearch()

    target_title = ""
    target_contents = ""
    pos_title_list = []
    pos_contents_list = []

    keyword_list = []
    related_company_list = []
    positive_score = 0

    ps = Positive()
    key = Keyword()
    com = Company()

    def __init__(self):
        print("init")


    def store(self,title,contents):
        self.target_title = title
        self.pos_title_list = self.get_morpheme(title)

        self.target_contents = contents
        self.pos_contents_list = self.get_morpheme(contents)

    def get_morpheme(self,text):
       setting = {
            "analyzer": "my_analyzer",
            "text": text,
            "attributes": ["posType", "leftPOS", "rightPOS", "morphemes", "reading"],
            "explain": "true"
        }
       i = IndicesClient(self.es)
       temp = i.analyze(index="pos", body=setting)
       tokens = temp.get('detail').get('tokenizer').get('tokens')
       token_list = list({token['token']: token for token in tokens}.values())  # 중복제거
       return token_list

    def get_positive(self):
        #positive score 초기화
        self.positive_score = 0
        self.positive_score = self.ps.get_positive(self.pos_title_list)
        return self.positive_score

    def get_keyword(self):
        #Keyword 초기화
        self.keyword_list=[]
        self.keyword_list = self.key.get_keyword(self.pos_title_list, self.pos_contents_list)
        return self.keyword_list

    def get_company(self):
        #Related company 초기화
        self.related_company_list = []
        self.related_company_list = self.com.get_realated_companies(self.keyword_list)
        return self.related_company_list

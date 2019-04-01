from konlpy.tag import Kkma

class Morpheme:
    kkma = Kkma()
    targetText = ""
    kkmaText = []

    def __init__(self):
        print("init")

    def store(self,text):
        self.targetText=text
        self.kkmaText = self.kkma.pos(self.targetText)
        print(self.kkmaText)


    def keyword(self):
        keywordDic = {}
        for morpheme in self.kkmaText :
            if keywordDic[morpheme] == "" :
                keywordDic[morpheme]=0
            else :
                keywordDic[morpheme]=keywordDic[morpheme]+1

        sorted(keywordDic, key=lambda k: keywordDic[k], reverse=True)
        keywords = list(keywordDic.keys())
        return keywords[0]


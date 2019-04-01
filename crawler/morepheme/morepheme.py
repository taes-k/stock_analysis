from konlpy.tag import Kkma

class Morpheme:
    kkma = Kkma()
    targetText = ""
    kkmaText = []

    def __init__(self):

    def setText(self,text):
        self.targetText=text
        self.kkmaText = Kkma.pos(targetText)

    def getKeyword(self):
        for morpheme in self.kkmaText :
            

        return
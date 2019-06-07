from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import csv

class Positive:
    texts=[]
    score=[]
    vectorizer = CountVectorizer(ngram_range=(1, 3),min_df=2) #tri-gram 까지 분석
    forest = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=2018)

    def __init__(self):
        self.positive_init()

        train_data = self.vectorizer.fit_transform(self.texts)
        train_data_array = train_data.toarray()
        self.forest.fit(train_data_array,self.score) #train data 학습

    def positive_init(self):
        with open('./crawler/morpheme/positiveTrainData_0607back.csv', 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.texts.append(row.get('text'))
                self.score.append(row.get('positive'))

    def get_positive(self,pos_title_list,company_list):
        text = ''
        pos_filter_list = ['NNG', 'XR', 'VV', 'VA', 'VP', 'MAG']

        for pos in pos_title_list:
            filter_check = False
            # pos Filtering
            for filter in pos_filter_list:
                if filter in pos.get('leftPOS'):
                    filter_check = True
                    break

            if filter_check:
                # 토큰이 상장기업명일시 필터링함
                if not (pos.get('token') in company_list):
                    # positive score text 조합
                    text = text + pos.get('token') + (pos.get('leftPOS').split('(')[0]) + ' '

        result = 0
        if text != '':

            target_data = [text]
            predict_data = self.vectorizer.transform(target_data)
            predict_data_array = predict_data.toarray()

            result = self.forest.predict(predict_data_array)
            result = int(result[0])

            # #훈련 데이터 업데이트
            # with open('./crawler/morpheme/positiveTrainData_0607back.csv', 'a') as csvfile:
            #     fieldnames = ['text', 'positive']
            #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #     data = {'text': text, 'positive': result}
            #     writer.writerow(data)

        return result

    def set_positive(self,title):

        print(title)
        i = input()

        if i!='3' :
            with open('./crawler/morpheme/positiveTrainData_0607back.csv', 'a') as csvfile:
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

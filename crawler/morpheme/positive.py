from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import csv

class Positive:
    texts=[]
    score=[]
    vectorizer = CountVectorizer(ngram_range=(1, 3),min_df=1) #tri-gram 까지 분석
    forest = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=2018)

    def __init__(self):
        self.positive_init()

        train_data = self.vectorizer.fit_transform(self.texts)
        train_data_array = train_data.toarray()
        self.forest.fit(train_data_array,self.score) #train data 학습

    def positive_init(self):
        with open('./crawler/morpheme/positiveTrainData.csv', 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.texts.append(row.get('text'))
                self.score.append(row.get('positive'))

    def get_positive(self,target):


        target_data = [target]
        predict_data = self.vectorizer.transform(target_data)
        predict_data_array = predict_data.toarray()

        result = self.forest.transform(predict_data_array)

        return result
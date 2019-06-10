# News Cralwer Stock Analysis

## 실행환경
- Python 3.7.3
- Django 2.1.7
- Elasticsearch 6.7.0

## 라이브러리
- Requests
- BeautifulSoup
- Scikit-learn
- Nori-analyzer
- Pandas
- Csv

- 한국예탁결제원 주식정보서비스api

## Demo
<http://www.stocknews.me>

## Example

<div>
<img width="500" src="https://github.com/taes-k/stock_analysis/raw/master/example_1.png">
<img width="500" src="https://github.com/taes-k/stock_analysis/raw/master/example_2.png">
</div>

## 개요
뉴스 기사 크롤링으로, 형태소 분석을 통해 상장기업들의 연관성 및 호재/악재를 분석하는 웹 서비스 프로젝트.

## 서비스 안내
### 형태소분석
Elasticsearch nori_analyzer  
user_dict에 상장기업 회사명들 사용자 사전 추가

###  키워드 추출
최다 빈도 명사형 단어 = 키워드 ( 단, 기사제목에 나온 명사형 단어에는 가중치를 부여 )
```c
NN(Count) = NN(Title) * 3 + NN(Contents) * 1
Keyword = Max(NN(Count))
```
### 호의적기사, 부정적기사 분석
CountVectorizer, RandomForest 사용.  
```c
#train data 학습
train_data = self.vectorizer.fit_transform(trainData)
train_data_array = train_data.toarray()
self.forest.fit(train_data_array,positiveScore)

#predict 예측
target_data = [target]
predict_data = self.vectorizer.transform(target_data)
predict_data_array = predict_data.toarray()

result = self.forest.predict(predict_data_array)
```
1000여개의 샘플 데이터를 바탕으로 Vector 화 시킨 뉴스Title 분석을 통해 Positive 점수를 매긴다.  
형태소를 Bi-gram, Tri-gram 까지 분석하여 정확도를 높인다.

### 관련주 검색
뉴스기사 학습을 통한 키워드-관련주 테이블 생성 
키워드 + Positive 점수 -> 관련주 점수

```
ex) 
Keyword : 미세먼지
Positive Score : -1

미세먼지 관련주

keyword  relationScore  company   totalScore
미세먼지        -10        나노       (-10)*(-55)
미세먼지        -5         오공       (-5)*(-55)
미세먼지        -3         모나리자    (-3)*(-55)
미세먼지        -2         코트렐     (-2)*(-55)

Result : [나노, 오공, 모나리자, 코트렐]
```

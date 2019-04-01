# News Cralwer Stock Analysis

## 실행환경
- Python 3.7.3
- Django 2.1.7
- Elasticsearch 6.7.0

## 라이브러리
- Requests
- BeautifulSoup
- KoNLPy
- Nori 분석기

- 한국예탁결제원 주식정보서비스api

## 개요
뉴스 기사 크롤링으로, 형태소 분석을 통해 상장기업들의 연관성 및 호재/악재를 분석하는 웹 서비스 프로젝트.

## 서비스 안내
###  키워드 추출
최다 빈도 명사형 단어 = 키워드 ( 단, 기사제목에 나온 명사형 단어에는 가중치를 부여한다 )
```c
NN(Count) = NN(Title) * 3 + NN(Contents) * 1
Keyword = Max(NN(Count))
```
### 호의적기사, 부정적기사 분석
KOSAC 감성사전 사용.  
뉴스기사 본문의 형태소단위로 쪼개어 명사, 동사 형태소들을 위 단어들로 매칭하여 Positive 점수로 매겨,    
0보다 크면 Positive, 0보다 작으면 Negative 으로 판단한다.

### 관련주 검색
키워드 + Positive 점수 -> 관련주 점수

```
ex) 
Keyword : 미세먼지
Positive Score : -55

미세먼지 관련주

keyword  relationScore  company   totalScore
미세먼지        -10        나노       (-10)*(-55)
미세먼지        -5         오공       (-5)*(-55)
미세먼지        -3         모나리자    (-3)*(-55)
미세먼지        -2         코트렐     (-2)*(-55)

```

import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
from crawler.morpheme.company import Company as CompanyModule


class Company:

    com = CompanyModule()

    def __init__(self):
        print("init")

    def getCompanyInfoByCode(self,_code):
        result = {}

        url = "https://finance.naver.com/item/main.nhn?code="+str(_code)


        request = requests.get(url);
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')

        total_info = soup.select('.new_totalinfo > .blind > dd')

        name = soup.select('#middle > div.h_company > div.wrap_company > h2 > a')[0]
        current_price = soup.select('#chart_area > div.rate_info > div > p.no_today > em > span.blind')[0]
        change = soup.select('#chart_area > div.rate_info > div > p.no_exday > em:nth-child(2) > span:nth-child(1)')[0]
        change = (change.text == '하락' and -1 or 1)
        change_price = soup.select('#chart_area > div.rate_info > div > p.no_exday > em:nth-child(2) > span.blind')[0]
        market = soup.select('.description > img')[0]

        change_percent = soup.select('#chart_area > div.rate_info > div > p.no_exday > em:nth-child(4) > span.blind')[0]

        yesterday_price = soup.select('#chart_area > div.rate_info > table.no_info > tr > td > em > span.blind')[0]
        start_price = soup.select('#chart_area > div.rate_info > table.no_info > tr > td > em > span.blind')[4]

        max_price = soup.select('#chart_area > div.rate_info > table.no_info > tr > td > em > span.blind')[1]
        min_price = soup.select('#chart_area > div.rate_info > table.no_info > tr > td > em > span.blind')[5]

        trade_count = soup.select('#chart_area > div.rate_info > table.no_info > tr > td > em > span.blind')[3]



        try :
            total_price = soup.select('#tab_con1 > div.first > table > tr.strong > td')
            total_price_text = total_price[0].text
            total_price_text = re.sub('\\t', '', total_price_text, 0, re.I | re.S)
            total_price_text = re.sub('\\n', '', total_price_text, 0, re.I | re.S)
            result['total_price'] = total_price_text
        except :
            result['total_price'] = "-"

        try :
            total_stock = soup.select('#_market_sum')[0]
            result['total_stock'] = int(re.sub(',','',total_stock.text,0,re.I | re.S))
        except :
            result['total_stock'] = 0

        try :
            year_max_price = soup.select('#tab_con1 > div:nth-child(4) > table > tr:last-child > td > em')[0]
            year_min_price = soup.select('#tab_con1 > div:nth-child(4) > table > tr:last-child > td > em')[1]
            result['year_max_price'] = int(re.sub(',','',year_max_price.text,0,re.I | re.S))
            result['year_min_price'] = int(re.sub(',','',year_min_price.text,0,re.I | re.S))
        except :
            result['year_max_price'] = 0
            result['year_min_price'] = 0

        result['date'] = datetime.strftime(datetime.now(timezone('Asia/Seoul')), "%Y-%m-%d %H:%M")
        result['code'] = _code
        result['name'] = name.text
        result['market'] = market['alt']
        result['current_price'] = int(re.sub(',','',current_price.text,0,re.I | re.S))
        result['change_price'] = int(re.sub(',','',change_price.text,0,re.I | re.S)) * change
        result['change_percent'] = float(change_percent.text) * change
        result['max_price'] = int(re.sub(',','',max_price.text,0,re.I | re.S))
        result['min_price'] = int(re.sub(',','',min_price.text,0,re.I | re.S))
        result['trade_count'] = int(re.sub(',','',trade_count.text,0,re.I | re.S))
        result['yesterday_price'] = int(re.sub(',','',yesterday_price.text,0,re.I | re.S))
        result['start_price'] = int(re.sub(',','',start_price.text,0,re.I | re.S))

        result['return_code'] = 200

        return result


    def getCompanyInfoByName(self,_name):
        code = self.com.get_company_code(_name)
        print("code error check :",code)
        if code == None :
            return {'return_code':400}
        return self.getCompanyInfoByCode(code)
import csv

class Company:
    company_dic = {}
    company_list = []
    company_realtion_keyword_dic = {}

    def __init__(self):
        self.company_init()

    def company_init(self):
        #상장기업 List init
        with open('./crawler/morpheme/listedCompanyList.csv', 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.company_list.append(row.get('name'))
                self.company_dic[row.get('name')] = row.get('code')
        #키워드 List init
        with open('./crawler/morpheme/positiveCompanyDic.csv', 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if self.company_realtion_keyword_dic.get(row.get('keyword')) == None:
                    self.company_realtion_keyword_dic[(row.get('keyword'))] = [{'name': row.get('company'), 'score': row.get('score')}]
                else:
                    duplication_check = False
                    for key_list in self.company_realtion_keyword_dic.get(row.get('keyword')) :
                        if row.get('company') == key_list.get('name') :
                            duplication_check = True
                    if not duplication_check :
                        list = self.company_realtion_keyword_dic.get(row.get('keyword'))
                        list.append({'name': row.get('company'), 'score': row.get('score')})
                        self.company_realtion_keyword_dic[(row.get('keyword'))] = list

    def get_realated_companies(self, keywords):
        filter_keywords = ['야구','축구','배구','별세','부고','인사','클로징','홈런']
        filter_check = False

        company_keyword_list = []
        company_score_dic = {}

        for filter in filter_keywords :
            if filter in keywords :
                filter_check = True

        if not filter_check :
            for keyword in keywords:
                print(self.company_realtion_keyword_dic.get(keyword) )
                #연관 키워드 dic 검색하여 score 점수 확인
                if self.company_realtion_keyword_dic.get(keyword) != None:
                    for company_info in self.company_realtion_keyword_dic.get(keyword):
                        if company_score_dic.get(company_info.get('name')) != None :
                            company_score_dic[company_info.get('name')] = company_score_dic[company_info.get('name')]+abs(float(company_info.get('score')))
                        else :
                            company_score_dic[company_info.get('name')] = abs(float(company_info.get('score')))
                        #중복방지를 위한 키워드리스트 생성
                        company_keyword_list.append(keyword+company_info.get('name'))

                #새로운 연관 키워드 생성
                if keyword in self.company_list :
                    company_name = keyword
                    for idx in range(0,2):
                        #기존에 없는 키워드일경우에만 저장
                        if not (keywords[idx]+company_name) in company_keyword_list :
                            #다른 회사 이름이 keyword일 경우 0.5점 , 기타 keyword일 경우 0.3점
                            score = (company_name == keywords[idx] and 1 or (keywords[idx] in self.company_list and 0.5 or 0.3))
                            data = {'keyword': keywords[idx], 'company': company_name, 'score': score}
                            with open('./crawler/morpheme/positiveCompanyDic.csv', 'a') as csvfile:
                                fieldnames = ['keyword','company','score']
                                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                                writer.writerow(data)

                            if company_score_dic.get(company_name) != None:
                                company_score_dic[company_name] = company_score_dic[company_name] + abs(score)
                            else:
                                company_score_dic[company_name] = abs(score)

        acc_company_list = sorted(company_score_dic.items(), key=lambda x: abs(x[1]), reverse=True)
        size = (3 if len(acc_company_list) >= 3 else len(acc_company_list))

        result_list = []
        for i in range(0, size):
            #0.8점 이상의 관련도를 갖은 회사명만 추출
            if acc_company_list[i][1] >= 0.9 :
                result_list.append({'name':acc_company_list[i][0],'code': self.company_dic.get(acc_company_list[i][0]) ,'score':acc_company_list[i][1]})

        return result_list

    def get_company_code(self, name):

        return self.company_dic.get(name)
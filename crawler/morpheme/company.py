import csv

class Company:

    company_list = []
    companydictionary = {}

    def __init__(self):
        self.company_init()

    def company_init(self):
        #상장기업 List init
        with open('./crawler/morpheme/listedCompanyList.csv', 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.company_list.append(row.get('name'))
        #키워드 List init
        with open('./crawler/morpheme/positiveCompanyDic.csv', 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if self.companydictionary.get(row.get('keyword')) == None:
                    self.companydictionary[(row.get('keyword'))] = [{'name': row.get('company'), 'score': row.get('score')}]
                else:
                    check = True
                    for keyList in self.companydictionary.get(row.get('keyword')) :
                        if row.get('company') == keyList.get('name') :
                            check = False

                    if check :
                        list = self.companydictionary.get(row.get('keyword'))
                        list.append({'name': row.get('company'), 'score': row.get('score')})
                        self.companydictionary[(row.get('keyword'))] = list

    def get_realated_companies(self, keywords):


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
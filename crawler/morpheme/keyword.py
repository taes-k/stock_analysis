class Keyword:
    def __init__(self):
        #keyword
        print('Init')

    def get_keyword(self,pos_title_list,pos_contents_list):
        keyword_dic = {}

        pos_filter_list = ['NNG','NNP','NP','SL']

        for pos in pos_title_list :
            filter_check = False
            # 품사 필터링
            for filter in pos_filter_list :
                if filter in pos.get('leftPOS'):
                    filter_check = True
                    break

            # Title에 나온 pos += 3점
            if filter_check :
                if keyword_dic.get(pos.get('token')) == None :
                    keyword_dic[pos.get('token')]=3
                else :
                    keyword_dic[pos.get('token')]=keyword_dic[pos.get('token')]+3

        for pos in pos_contents_list:
            filter_check = False
            # pos Filtering
            for filter in pos_filter_list :
                if filter in pos.get('leftPOS'):
                    filter_check = True
                    break

            #Contents에 나온 pos += 1점
            if filter_check:
                if keyword_dic.get(pos.get('token')) == None:
                    keyword_dic[pos.get('token')] = 1
                else:
                    keyword_dic[pos.get('token')] = keyword_dic[pos.get('token')] + 1


        #최대 5개 키워드 추출
        acc_keyword_list =sorted(keyword_dic.items(),key=lambda x: x[1], reverse=True)
        size = (5 if len(acc_keyword_list)>=5 else len(acc_keyword_list))

        result_list = []
        for i in range(0,size) :
            result_list.append(acc_keyword_list[i][0])

        return result_list
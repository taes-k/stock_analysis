from company.module.company import Company
from django.http import HttpResponse, JsonResponse

def getCompanyInfo(request):
    company = Company()
    name = None
    code = None

    try:
        code = request.GET['code']
    except:
        name = request.GET['name']

    print("CODE : ",code)
    print("name : ",name)
    if code != None:
        result = JsonResponse(company.getCompanyInfoByCode(code))
    else :
        result = JsonResponse(company.getCompanyInfoByName(name))


    return result
from company.module.company import Company
from django.http import HttpResponse, JsonResponse

def getCompanyInfo(request):
    company = Company()

    print("name ::", request.GET['name'])
    result = JsonResponse(company.getCompanyInfoByCode(request.GET['code']))
    return result
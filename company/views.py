from company.module.company import Company
from django.http import HttpResponse, JsonResponse

def getCompanyInfo(request):
    company = Company()
    result = JsonResponse(company.getCompanyInfo(request.GET['company']))
    return result
from django.http import JsonResponse
from common import utils
def verify_phone(request):
    phone_num = request.POST.get('phone_num')

    if utils.is_phone_num(phone_num.strip()):
        pass

    return JsonResponse({'code':1001,'data':None})
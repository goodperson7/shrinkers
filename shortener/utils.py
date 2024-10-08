from shortener.models import Users,ShorteneUrls
from django.db.models import F
from django.http.response import JsonResponse
from rest_framework.response import Response
from datetime import datetime, timedelta

def url_count_changer(request, is_increase:bool):
    count_number = 1 if is_increase else -1
    Users.objects.filter(user_id=request.user.id).update(url_count=F("url_count") + count_number)

def MsgOk(status:int = 200):
    return Response({"msg":"ok"}, status=status)

def get_kst():
    return datetime.now() + timedelta(hours=9)
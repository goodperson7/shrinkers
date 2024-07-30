from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here. 

def index(request):
    user = User.objects.filter(username="admin").first()
    email = user.email if user else "Anonymous User!"

    return render(request, "base.html",{"welcom_msg":"Hello {email}"})
 

@csrf_exempt
def get_user(request, user_id):
    print(user_id)
    if request.method == "GET":
        abc = request.GET.get("abc")
        xyz = request.GET.get("xyz")
        user = User.objects.filter(id=user_id).first()
        return render(request, "base.html", {"user": user, "params": [abc,xyz]})
    elif request.method == "POST":
        username = request.GET.get("username")
        if username:
            user = User.objects.filter(pk=user_id).update(username=username)
        return JsonResponse(status=201, data=dict(msg="User updated successfully!"), safe=False)



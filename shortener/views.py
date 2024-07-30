from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm, PasswordChangeForm,AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterFrom 

# Create your views here. 

def index(request):
    user = User.objects.filter(username="admin").first()
    email = user.email if user else "Anonymous User!"
    if request.user.is_authenticated:
        email = "Anonymous User!"
    return render(request, "base.html",{"welcom_msg":f"Hello {email}"})
 

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
    
def register(request):
    if request.method == "POST":

        form = RegisterFrom(request.POST)
        msg = "올바르지 않은 데이터 입니다."   
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return render(request, "register.html", {"form": form, "msg": msg})
    else:
        form = RegisterFrom()

        return render(request, "register.html", {"form": form})
    
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        msg = "가입되어 있지 않거나 로그인 정보가 잘못 되었습니다."
        print(form.is_valid)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                msg = "로그인 성공"
                login(request, user)
        return render(request, "login.html", {"form": form, "msg": msg})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
    
def logout_view(request):
    logout(request)
    return redirect("index")
                





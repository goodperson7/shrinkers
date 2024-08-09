from django import forms
from shortener.utils import url_count_changer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ShorteneUrls 
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):
    last_name = forms.CharField(max_length=50, required=False, help_text="Optional", label="이름")
    username = forms.CharField(max_length=50, required=True, help_text="Optional", label="아이디")
    email = forms.EmailField(max_length=254, required=True, help_text="Required. Inform a valid email address.")

    class Meta:
        model = User
        fields = ('username', 'last_name', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "이메일"}) 
    )
    password = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "비밀번호"})
    )
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input","id":"_loginRememberMe"}),
        disabled=False
    )

class UrlCreateForm(forms.ModelForm):
    class Meta:
        model = ShorteneUrls
        fields = ["nick_name", "target_url"]
        labels = {
            "nick_name": _("닉네임"),
            "target_url": _("URL"),
        }
        widgets = {
            "nick_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "URL을 구분하기 위한 별칭"}),
            "target_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "포워딩될 URL"}),
        }   

    def save(self, request, commit=True):
        instance = super(UrlCreateForm, self).save(commit=False)
        instance.creator_id = request.user.id
        instance.target_url = instance.target_url.strip()
        if commit:
            try:
                instance.save()
            except Exception as e:
                print(e)
            else:
                url_count_changer(request, True) 
        return instance
    
    def update_form(self, request, url_id):
        instance = super(UrlCreateForm,self).save(commit=False)
        instance.target_url = instance.target_url.strip()
        ShorteneUrls.objects.filter(pk=url_id, created_by_id=request.user.id).update(
            nick_name=instance.nick_name,
            target_url=instance.target_url
        )
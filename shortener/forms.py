from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterFrom(UserCreationForm):
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

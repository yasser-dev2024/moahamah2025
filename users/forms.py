from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CustomUser._meta.get_field('user_type').choices, label="نوع المستخدم")
    phone = forms.CharField(max_length=15, required=False, label="رقم الجوال")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'user_type', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="اسم المستخدم")
    password = forms.CharField(widget=forms.PasswordInput, label="كلمة المرور")

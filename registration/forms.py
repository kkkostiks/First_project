from sys import platform

from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'reg-info', "placeholder": "Логін"}),
            'first_name': TextInput(attrs={'class': 'reg-info', "placeholder": "ім'я"}),
            'last_name': TextInput(attrs={'class': 'reg-info', "placeholder": "Прізвище"}),
            'email': EmailInput(attrs={'class': 'reg-info' , "placeholder": "Емейл"}),
            'password': PasswordInput(attrs={'class': 'reg-info', "placeholder": "Пароль"})
        }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username':TextInput(attrs={'class': 'reg-info', 'placeholder': "Логін"}),
            'password': PasswordInput(attrs={'class': 'reg-info', "placeholder": "Пароль"})
        }
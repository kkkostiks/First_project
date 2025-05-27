from sys import platform
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, ValidationError, CharField
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



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

    def clean_username(self):
        new_username = self.cleaned_data['username']
        if User.objects.filter(username=new_username).exists():
            raise ValidationError("Користувач з таким логіном вже існує")
        return new_username


class LoginForm(forms.Form):
        username = CharField(widget=forms.TextInput(attrs={'class': 'reg-info', 'placeholder': "Логін"}))
        password = CharField(widget=forms.PasswordInput(attrs={'class': 'reg-info', 'placeholder': "Пароль"}))

        def clean(self):
            cleaned_data = super(LoginForm, self).clean()
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise ValidationError("Невірний логін чи пароль")
            self.user = user
            return cleaned_data



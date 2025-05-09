from dbm import error
from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache


# Create your views here.
@never_cache
def reg(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Користувач з таким логіном уже існує')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('authentication')
        else:
           messages.error(request, "Ви ввели щось не те")

    data = {
        'form' :  UserForm(),
    }

    return render(request, 'registration/registration.html', data)


@never_cache
def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Ви ввели щось не те")
            return redirect('authentication')

    data = {
        'form' : LoginForm(),
    }

    return render(request,'registration/auth.html', data)


def logout_user(request):
    logout(request)
    messages.success(request, "Ви вийшли з акаунту")
    return redirect('home')

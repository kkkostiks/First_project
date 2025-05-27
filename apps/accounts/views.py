from dbm import error
from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache


# Create your views here.
@never_cache
def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
            user.save()
            return redirect('authentication')
        else:
            return render(request, 'accounts/registration.html', { 'form': form})
    return render(request, 'accounts/registration.html', {'form': UserForm()})

@never_cache
def authentication(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if  form.is_valid():
            user = form.user
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/authentication.html', { 'form': form})
    return render(request,'accounts/authentication.html', {'form' : LoginForm(),})


def logout_user(request):
    logout(request)
    messages.success(request, "Ви вийшли з акаунту")
    return redirect('home')

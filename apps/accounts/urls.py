from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('authentication', views.authentication, name='authentication'),
    path('logout', views.logout_user, name='logout')
]
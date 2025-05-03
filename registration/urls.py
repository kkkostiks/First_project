from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.reg, name='registration'),
    path('authentication', views.auth, name='authentication'),
    path('logout', views.logout_user, name='logout')
]
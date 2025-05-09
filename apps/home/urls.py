
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book', views.book, name='book'),
    path('book-card/<int:pk>/', views.BooksDetailView.as_view(), name='book-card'),
    path('book-card/<int:pk>/update', views.BooksUpdateView.as_view(), name='book-card-update'),
    path('book-card/<int:pk>/delete', views.BooksDeleteView.as_view(), name='book-card-delete'),
]
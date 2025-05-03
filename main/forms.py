from array import array

from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, FileInput, NumberInput
from .models import Books

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'author', 'year', 'datetime', 'text', 'foto')
        widgets = {
            'title': TextInput(attrs={'class': 'book-info', 'placeholder': 'Назва'}),
            'author': TextInput(attrs={'class': 'book-info', 'placeholder': 'Автор'}),
            'year': NumberInput(attrs={'class': 'book-info', 'placeholder': 'рік написання'}),
            'datetime': DateTimeInput(attrs={'class': 'book-info', 'placeholder': 'Дата', 'type': 'datetime-local'}),
            'text' : Textarea(attrs={'class': 'description', 'placeholder': 'Опис'}),
            'foto' : FileInput(attrs={'class': 'foto', 'placeholder': 'Фото'})
        }

class SearchBookForm(ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'author', 'year', 'text',)
        widgets = {
            'title' : TextInput(attrs={
                'class': 'input', 'placeholder': 'Знайдіть книгу'
            })
        }
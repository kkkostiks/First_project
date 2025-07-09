from array import array
from datetime import datetime

from django.utils.translation import gettext as _
from django.db.models import Q
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, FileInput, NumberInput, Form
from django import forms
from .models import Books


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'author', 'publishing_house', 'language', 'count_pages', 'year', 'publish_year', 'datetime', 'text', 'foto', 'file')
        widgets = {
            'title': TextInput(attrs={'class': 'book-info', 'placeholder': _('Назва')}),
            'author': TextInput(attrs={'class': 'book-info', 'placeholder': _('Автор')}),
            'publishing_house': TextInput(attrs={'class': 'book-info', 'placeholder': _('Видавництво')}),
            'language': TextInput(attrs={'class': 'book-info', 'placeholder': _('Мова')}),
            'count_pages': NumberInput(attrs={'class': 'book-info', 'placeholder': _('Кількість сторінок')}),
            'year': NumberInput(attrs={'class': 'book-info', 'placeholder': _('Рік видання')}),
            'publish_year': NumberInput(attrs={'class': 'book-info', 'placeholder': _('Рік написання')}),
            'datetime': DateTimeInput(attrs={'class': 'book-info', 'placeholder': _('Дата'), 'type': 'datetime-local'}),
            'text' : Textarea(attrs={'class': 'description', 'placeholder': _('Опис')}),
            'foto' : FileInput(attrs={'class': 'foto', 'placeholder': _('Фото')}),
            'file': FileInput(attrs={'class': 'foto', 'placeholder': _('Файл')}),

        }

class SearchBookForm(forms.Form):
    term = forms.CharField(required=False, widget=TextInput(attrs={"class": "input", "placeholder": _("Знайдіть книгу")}))
    publishing_house = forms.CharField(required=False, widget=TextInput(attrs={"class": "modal-input", "placeholder": _("Введіть видавництв")}))
    count_pages_from = forms.IntegerField(required=False, widget=NumberInput(attrs={"class": "modal_number_input", "placeholder": _("Введіть кількість сторінок")}))
    count_pages_to = forms.IntegerField(required=False, widget=NumberInput(attrs={"class": "modal_number_input", "placeholder": _("Введіть кількість сторінок")}))
    publish_year_from = forms.IntegerField( required=False,
        widget=NumberInput(attrs={"class": "modal_number_input", "placeholder": _("Введіть рік")}))
    publish_year_to = forms.IntegerField(required=False,
        widget=NumberInput(attrs={"class": "modal_number_input", "placeholder": _("Введіть рік")}))
    year_from = forms.IntegerField(required=False,
        widget=NumberInput(attrs={"class": "modal_number_input", "placeholder": _("Введіть рік")}))
    year_to = forms.IntegerField(required=False,
        widget=NumberInput(attrs={"class": "modal_number_input", "placeholder": _("Введіть рік")}))
    datetime_from = forms.DateTimeField(required=False,
        widget= DateTimeInput(attrs={'class': 'modal_number_input', 'placeholder': _('Дата'), 'type': 'datetime-local'}))
    datetime_to = forms.DateTimeField(required=False,
        widget=DateTimeInput(attrs={'class': 'modal_number_input', 'placeholder': _('Дата'), 'type': 'datetime-local'}))


    def clean(self):
        return self.cleaned_data

    def get_query(self, books):
        term = self.cleaned_data.get('term', '').strip()
        count_pages_from = self.cleaned_data.get('count_pages_from', '')
        count_pages_to = self.cleaned_data.get('count_pages_to', '')
        datetime_from = self.cleaned_data.get('datetime_from', '')
        datetime_to = self.cleaned_data.get('datetime_to', '')
        publish_year_from = self.cleaned_data.get('publish_year_from', '')
        publish_year_to = self.cleaned_data.get('publish_year_to', '')
        year_from = self.cleaned_data.get('year_from', '')
        year_to = self.cleaned_data.get('year_to', '')


        if term:
            books = books.filter(Q(title__icontains=term) | Q(author__icontains=term) |
                      Q(text__icontains=term) | Q(publishing_house__icontains=term) | Q(language__icontains=term) )

        if count_pages_from is not None:
            books = books.filter(count_pages__gte=count_pages_from)

        if count_pages_to is not None:
            books = books.filter(count_pages__lte=count_pages_to)

        if datetime_from:
            books = books.filter(datetime__gte=datetime_from)

        if datetime_to:
            books = books.filter(datetime__lte=datetime_to)

        if publish_year_from is not None:
            books = books.filter(publish_year__gte=publish_year_from)

        if publish_year_to is not None:
            books = books.filter(publish_year__lte=publish_year_to)

        if year_from is not None:
            books = books.filter(year__gte=year_from)

        if year_to is not None:
            books = books.filter(year__lte=year_to)

        return books
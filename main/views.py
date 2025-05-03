from django.shortcuts import render, redirect
from select import error
from .forms import BooksForm, SearchBookForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Books
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.decorators.cache import never_cache
from django.db.models import Q
# Create your views here.

def home(request):
    books = None
    is_book = 0
    form = SearchBookForm(request.POST)
    if request.user.is_authenticated:
        books = Books.objects.filter(user=request.user)
        if books:
            is_book = 1
        if request.method == 'POST':
            title = request.POST.get('title').strip()
            if title:
                is_book = 2
                books = Books.objects.filter(Q(title__icontains=title) |
                                             Q(author__icontains=title) |
                                             Q(year__icontains=title) |
                                             Q(text__icontains=title)
                                             ,user=request.user,).order_by('title')
                if not books:
                    is_book = 3


    data = {
        'books': books,
        'form': form,
        'is_book': is_book,
    }
    return render(request, 'main/home.html', data)

@never_cache
def book(request):
   if request.method == 'POST':
      form = BooksForm(request.POST, request.FILES)
      if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')

   data = {
      'form':  BooksForm(),
       'title': "Додавання книги"
   }
   return render(request, 'main/book.html', data)


class BooksDetailView(DetailView):
    model = Books
    template_name = 'main/book-card.html'
    context_object_name = 'book_card'

    def get_queryset(self):
        return Books.objects.filter(user=self.request.user)

class BooksUpdateView(UpdateView):
    model = Books
    form_class = BooksForm
    template_name = 'main/update-book.html'
    context_object_name = 'book_update'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_name_update'] = f"Редагування книги {self.object.title}"
        return context

class BooksDeleteView(DeleteView):
    model = Books
    template_name = 'main/delete_book.html'
    success_url = '/'
    context_object_name = 'book_delete'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_name_delete'] = f"видалення книги {self.object.title}"
        return context
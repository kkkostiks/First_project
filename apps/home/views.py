from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from select import error
from .forms import BooksForm, SearchBookForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Books
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.decorators.cache import never_cache
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils.translation import gettext as _
# Create your views here.

# @login_required(login_url='authentication')
def home(request):
    if not request.user.is_authenticated:
        return render(request, "home/home.html")
    form = SearchBookForm(request.POST or None)
    books = Books.objects.filter(user=request.user)
    if request.method == "POST" and form.is_valid():
        books = form.get_query(books).order_by('title')
    print(form.errors)
    paginator = Paginator(books, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, "home/home.html", {
                                            'books': books,
                                            'form': form,
                                            'page_obj': page_obj,})

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
       'title': _("Додавання книги")
   }
   return render(request, 'home/book.html', data)


class BooksDetailView(DetailView):
    model = Books
    template_name = 'home/book-card.html'
    context_object_name = 'book_card'

    def get_queryset(self):
        return Books.objects.filter(user=self.request.user)

class BooksUpdateView(UpdateView):
    model = Books
    form_class = BooksForm
    template_name = 'home/update-book.html'
    context_object_name = 'book_update'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_name_update'] = _(f"Редагування книги {self.object.title}")
        return context

class BooksDeleteView(DeleteView):
    model = Books
    template_name = 'home/delete_book.html'
    success_url = '/'
    context_object_name = 'book_delete'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_name_delete'] = _(f"видалення книги {self.object.title}")
        return context
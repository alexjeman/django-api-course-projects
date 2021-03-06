from django.shortcuts import render
from django.views.generic import ListView

from apps.books.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

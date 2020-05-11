from django.shortcuts import render
from datetime import datetime
from books.models import Book
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    our_context = {"time":datetime.now()}
    return render(request,template_name="index.html",context=our_context)


def list_books(request):
    books = Book.objects.all
    context = {
        "books":books
    }
    return render(request, template_name="book_list.html", context=context)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
<<<<<<< HEAD
    Book_list = Book.objects.all()
    return HttpResponse(Book_list)
=======
    book_list = Book.objects.all()
    context={
        'book_list':book_list
    }
    return render(request,'Myapp/index.html',context)


def detail(request,id):
    return HttpResponse('this is detail %s' %id)


>>>>>>> 65f4bf3 (This is my first Django project)

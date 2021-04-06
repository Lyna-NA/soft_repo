from django.shortcuts import render
#from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    members_num=Member.objects.all().count()
    books_num=Book.objects.all().count()
    nonReturned_books_num=Book.objects.all().filter(status='available').count()
    context={'members_num':members_num,'books_num':books_num,'nonReturned_books_num':nonReturned_books_num}
    return render(request,'admin/home.html',context) 

def errorPage(request):
    return render(request,'admin/404.html') 

def addBook(request):
    return render(request,'admin/addBook.html') 

def addCat(request):
    return render(request,'admin/addCat.html') 

def addShelf(request):
    return render(request,'admin/addShelf.html') 

def blank(request):
    return render(request,'admin/blank.html') 

def booksList(request):
    books=Book.objects.all()
    return render(request,'admin/booksList.html',{'books': books}) 

def catList(request):
    return render(request,'admin/catList.html') 

def createIssue(request):
    return render(request,'admin/createIssue.html') 

def forgot_password(request):
    return render(request,'admin/forgot-password.html') 

def issuesList(request):
    return render(request,'admin/issuesList.html') 

def login(request):
    return render(request,'admin/login.html') 

def non_returnedBooks(request):
    return render(request,'admin/non_returnedBooks.html') 

def profileManger(request):
    return render(request,'admin/profileManger.html') 

def profileMember(request):
    return render(request,'admin/profileMemember.html')

def register(request):
    return render(request,'admin/register.html') 

def managersList(request):
    return render(request,'admin/managersList.html') 

def membersList(request):
    return render(request,'admin/membersList.html') 

def addUser(request):
    return render(request,'admin/addUser.html') 
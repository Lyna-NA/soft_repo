from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'admin/home.html') 

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
    return render(request,'admin/booksList.html') 

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
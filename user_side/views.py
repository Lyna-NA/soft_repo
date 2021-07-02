from django.shortcuts import render
from django.views.generic import View
from management_side.models import *
from django.shortcuts import get_list_or_404, render,redirect,get_object_or_404
from django.contrib.auth import authenticate  , logout
from registration.decorators import notLoggedUsers , allowedUsers
from django.contrib import messages
from django.contrib.auth.decorators import  login_required


# Create your views here.
@allowedUsers('customer')
@login_required(login_url='signin')
def user_dashboard(request):
    books = Book.objects.all()
    booksNum = books.count()
    
    context ={
         'booksNum': booksNum,
   

    }

    if request.method == 'GET': 
        return render(request ,'userSide/user_dashboard.html',context)

def index(request):
    b =Manager.objects.all()
    managersNum = b.count()
    books = Book.objects.all()
    booksNum = books.count()
    customer = Customer.objects.all()
    customerNum = customer.count()
    issue = Issue.objects.all()
    issueNum = issue.count()
    
    eng =get_list_or_404(Book, language = 'English' )    
    context ={
    'manager' : b,
    'booksNum': booksNum,
    'managersNum':managersNum,
    'customerNum':customerNum,
    'issueNum':issueNum,
    'eng' : eng,

    }
    if request.method == 'GET': 
        return render(request ,'userSide/index.html' , context)

@allowedUsers('customer')
@login_required(login_url='signin')
def books(request):
    i = None
    b =Book.objects.all()
    if 'searchname' in request.GET :
        i = request.GET['searchname']
        if i:
            b =b.filter(isbn__icontains=i)
    context ={
    'books' : b,
    'isbn' :i,
    }

    return render(request, 'userSide/books.html',context)
@notLoggedUsers
def books2(request):
    books = Book.objects.all()

    return render(request, 'userSide/books2.html', {'books': books})   
@allowedUsers('customer')
@login_required(login_url='signin')
def bookInfo(request, book_id):
    cnntext = { 
        'book_id' :get_object_or_404(Book,pk = book_id)
        }

    
    return render(request, 'userSide/bookInfo.html', cnntext)
@notLoggedUsers
def bookInfo2(request, book_id):
    cnntext = { 
        'book_id' :get_object_or_404(Book,pk = book_id)
        }

    
    return render(request, 'userSide/bookInfo2.html', cnntext)
@allowedUsers('customer')
@login_required(login_url='signin')
def issue(request , username):
    o = get_object_or_404(Customer , username = username )
    
    issues =get_list_or_404(Issue, customer = o )
    
    
    return render(request,'userSide/issue.html',{'issues':issues})

    
@allowedUsers('customer')
@login_required(login_url='signin')
def notReturned(request , username):
    o = get_object_or_404(Customer , username = username )
    
    issues =get_list_or_404(Issue, customer = o  )
    
    
    
    return render(request,'userSide/notReturned.html',{'issues':issues})
@allowedUsers('customer')
@login_required(login_url='signin')
def logoutCustomer(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'logout succesfully')
    return redirect('signin')
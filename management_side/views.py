from django.shortcuts import render,redirect
from .models import *
from .forms import IssueForm,CustomerForm
from django.contrib.auth.decorators import  login_required
from registration.decorators import allowedUsers 

@login_required(login_url='login')
@allowedUsers(allowedGroups=['manager','admin'])
#@formanagements
def home(request):
    customers_num=Customer.objects.all().count()
    books_num=Book.objects.all().count()
    nonReturned_books_num=Book.objects.all().filter(status='available').count()
    context={'customers_num':customers_num,'books_num':books_num,'nonReturned_books_num':nonReturned_books_num}
    return render(request,'management/home.html',context) 


def errorPage(request):
    return render(request,'management/404.html') 

def addBook(request):
    return render(request,'management/addBook.html') 

def addCat(request):
    return render(request,'management/addCat.html') 

# def addShelf(request):
#     return render(request,'management/addShelf.html') 

def blank(request):
    return render(request,'management/blank.html') 

def booksList(request):
    books=Book.objects.all()
    return render(request,'management/booksList.html',{'books': books}) 

def catList(request):
    return render(request,'management/catList.html') 


@login_required(login_url='login')
@allowedUsers(allowedGroups=['manager'])
def createIssue(request):
    form=IssueForm()
    if request.method=='POST':
        form=IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'management/createIssue.html',context) 


@login_required(login_url='login')
@allowedUsers(allowedGroups=['manager'])
def updateIssue(request,pk):
    issue=Issue.objects.get(id=pk)
    form=IssueForm(instance=issue)
    if request.method=='POST':
        form=IssueForm(request.POST,instance=issue)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'management/createIssue.html',context) 


@login_required(login_url='login')
@allowedUsers(allowedGroups=['manager','admin'])
def deleteIssue(request,pk):
    issue=Issue.objects.get(id=pk)
    if request.method=='POST':
        issue.delete()
    context={'issue':issue}
    return render(request,'management/deleteIssue.html',context) 


def forgot_password(request):
    return render(request,'management/forgot-password.html') 


@login_required(login_url='login')
@allowedUsers(allowedGroups=['manager'])
def issuesList(request):
    issues=Issue.objects.all()
    context={'issues':issues}
    return render(request,'management/issuesList.html',context) 

@allowedUsers(allowedGroups=['manager'])
def managersList(request):
    managers=Issue.objects.all()
    context={'managers':managers}
    return render(request,'management/managersList.html',context) 


@allowedUsers(allowedGroups=['manager','admin'])
def customersList(request):
    customer=Issue.objects.all()
    context={'customer':customer}
    return render(request,'management/customersList.html',context) 



# def login(request):
#     return render(request,'management/login.html') 


@login_required(login_url='login')
@allowedUsers(allowedGroups=['manager'])
def non_returnedBooks(request):
    return render(request,'management/non_returnedBooks.html') 


@login_required(login_url='login')
@allowedUsers(allowedGroups=['manager'])
def managerProfile(request):
    return render(request,'management/managerProfile.html') 


# def customerProfile(request,pk):   #بتفيد في ال issues
#     member =Member.objects.get(id=pk)
#     orders=member.order_set.all()
#     num_order=orders.count()
#     context={'member': member,'orders':orders}
#     return render(request,'management/customerProfile.html',{'member':member})


# def register(request):
#     return render(request,'management/register.html') 

def addUser(request):
    return render(request,'management/addUser.html') 


@login_required(login_url='login')
@allowedUsers(allowedGroups=['customer'])
def customerProfile(request):   
    # customer =Customer.objects.get(id=pk)
    customer =request.user.customer
#    orders=member.order_set.all()
#    num_order=orders.count()
 #   context={'member': member,'orders':orders}
    form = CustomerForm(instance=customer)
    if request.method == 'POST': 
        form = CustomerForm(request.POST , request.FILES, instance=customer)
        if form.is_valid():
            form.save() 
    return render(request,'management/customerProfile.html',{'form':form})

def profile(request):   
    group =  request.user.groups.all()[0].name
    print(group)
    if group == 'customer':
       return redirect('customerProfile')
    if group == 'manager' or group=='admin':
       return redirect('managerProfile')

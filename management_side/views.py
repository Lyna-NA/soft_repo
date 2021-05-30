from django.shortcuts import render,redirect
from .models import *
from .forms import IssueForm
from django.contrib.auth.decorators import  login_required


@login_required(login_url='login')
# #@allowedUsers(allowedGroups=['management'])
#@formanagements
def home(request):
    members_num=Member.objects.all().count()
    books_num=Book.objects.all().count()
    nonReturned_books_num=Book.objects.all().filter(status='available').count()
    context={'members_num':members_num,'books_num':books_num,'nonReturned_books_num':nonReturned_books_num}
    return render(request,'management/home.html',context) 

def errorPage(request):
    return render(request,'management/404.html') 

# def addBook(request):
#     return render(request,'management/addBook.html') 

# def addCat(request):
#     return render(request,'management/addCat.html') 

# def addShelf(request):
#     return render(request,'management/addShelf.html') 

def blank(request):
    return render(request,'management/blank.html') 

def booksList(request):
    books=Book.objects.all()
    return render(request,'management/booksList.html',{'books': books}) 

def catList(request):
    return render(request,'management/catList.html') 

def createIssue(request):
    form=IssueForm()
    if request.method=='POST':
        form=IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'management/createIssue.html',context) 

def updateIssue(request,pk):
    issue=Issue.objects.get(id=pk)
    form=IssueForm(instance=issue)
    if request.method=='POST':
        form=IssueForm(request.POST,instance=issue)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'management/createIssue.html',context) 

def deleteIssue(request,pk):
    issue=Issue.objects.get(id=pk)
    if request.method=='POST':
        issue.delete()
    context={'issue':issue}
    return render(request,'management/deleteIssue.html',context) 

def forgot_password(request):
    return render(request,'management/forgot-password.html') 

def issuesList(request):
    issues=Issue.objects.all()
    context={'issues':issues}
    return render(request,'management/issuesList.html',context) 

def managersList(request):
    managers=Issue.objects.all()
    context={'managers':managers}
    return render(request,'management/managersList.html',context) 

# def login(request):
#     return render(request,'management/login.html') 

def non_returnedBooks(request):
    return render(request,'management/non_returnedBooks.html') 

def profileManager(request):
    return render(request,'management/profileManager.html') 

def profileMember(request,pk):   #بتفيد في ال issues
    member =Member.objects.get(id=pk)
    orders=member.order_set.all()
    num_order=orders.count()
    context={'member': member,'orders':orders}
    return render(request,'management/profileMember.html',{'member':member})

# def register(request):
#     return render(request,'management/register.html') 

def managersList(request):
    return render(request,'management/managersList.html') 

def membersList(request):
    member=Member.objects.all()
    return render(request,'management/membersList.html',{'member':member}) 

# def addUser(request):
#     return render(request,'management/addUser.html') 

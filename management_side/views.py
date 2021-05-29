from django.shortcuts import render,redirect

#from django.http import HttpResponse
from .models import *
from .forms import IssueForm

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
    form=IssueForm()
    if request.method=='POST':
        form=IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'admin/createIssue.html',context) 

def updateIssue(request,pk):
    issue=Issue.objects.get(id=pk)
    form=IssueForm(instance=issue)
    if request.method=='POST':
        form=IssueForm(request.POST,instance=issue)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'admin/createIssue.html',context) 

def forgot_password(request):
    return render(request,'admin/forgot-password.html') 

def issuesList(request):
    issues=Issue.objects.all()
    context={'issues':issues}
    return render(request,'admin/issuesList.html',context) 

def login(request):
    return render(request,'admin/login.html') 

def non_returnedBooks(request):
    return render(request,'admin/non_returnedBooks.html') 

def profileManager(request):
    return render(request,'admin/profileManager.html') 

def profileMember(request,pk):   #بتفيد في ال issues
    member =Member.objects.get(id=pk)
#    orders=member.order_set.all()
#    num_order=orders.count()
 #   context={'member': member,'orders':orders}
    return render(request,'admin/profileMember.html',{'member':member})

def register(request):
    return render(request,'admin/register.html') 

def managersList(request):
    return render(request,'admin/managersList.html') 

def membersList(request):
    member=Member.objects.all()
    return render(request,'admin/membersList.html',{'member':member}) 

def addUser(request):
    return render(request,'admin/addUser.html') 

    # بفيد  في ال issue
    # بقدر اعمل 
    # .book.category متلا
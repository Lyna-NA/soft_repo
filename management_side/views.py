from django.shortcuts import render,redirect
from .models import *
from .forms import IssueForm,CustomerForm,ManagerForm
from django.contrib.auth.decorators import  login_required
from registration.decorators import allowedUsers 


def home(request):   
    if request.user.groups.exists():
        group =  request.user.groups.all()[0].name
        print(group)
        if group == 'customer':
            return redirect('user_dashboard')
        if group == 'manager' or group=='admin':
            return redirect('manager_dashboard')
    return redirect('signin')


#@formanagements
@login_required(login_url='signin')
@allowedUsers(allowedGroups=['manager'])
def manager_dashboard(request):
    customers_num=Customer.objects.all().count()
    books_num=Book.objects.all().count()
    nonReturned_books_num=Book.objects.all().filter(status='available').count()
    context={'customers_num':customers_num,'books_num':books_num,'nonReturned_books_num':nonReturned_books_num}
    return render(request,'management/manager_dashboard.html',context) 


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


@login_required(login_url='signin')
@allowedUsers(allowedGroups=['manager'])
def createIssue(request):
    form=IssueForm()
    if request.method=='POST':
        form=IssueForm(request.POST)
        form.manager=request.user.id
        if form.is_valid():
            form.save()
            return redirect('issuesList')
    context={'form':form}
    return render(request,'management/createIssue.html',context) 


@login_required(login_url='signin')
@allowedUsers(allowedGroups=['manager'])
def updateIssue(request,pk):
    issue=Issue.objects.get(issue_id=pk)
    #book_status=Issue.objects.get(book_id=issue.issue_id)
    form=IssueForm(instance=issue)      
    form.manager=request.user.id
    
    if request.method=='POST':
        form=IssueForm(request.POST,instance=issue)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'management/updateIssue.html',context) 


@login_required(login_url='signin')
@allowedUsers(allowedGroups=['manager','admin'])
def deleteIssue(request,pk):
    issue=Issue.objects.get(issue_id=pk)
    if request.method=='POST':
        issue.delete()
    context={'issue':issue}
    return render(request,'management/deleteIssue.html',context) 


def forgot_password(request):
    return render(request,'management/forgot-password.html') 


@login_required(login_url='signin')
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


@login_required(login_url='signin')
@allowedUsers(allowedGroups=['manager'])
def non_returnedBooks(request):
    return render(request,'management/non_returnedBooks.html') 


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


@login_required(login_url='signin')
@allowedUsers(allowedGroups=['customer'])
def customerProfile(request):   
    customer =request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST': 
        form = CustomerForm(request.POST , request.FILES, instance=customer)
        if form.is_valid():
            form.save() 
    return render(request,'userSide/customerProfile.html',{'form':form})



@login_required(login_url='signin')
@allowedUsers(allowedGroups=['manager'])
def managerProfile(request):
    manager =request.user.manager
    form = ManagerForm(instance=manager)
    if request.method == 'POST': 
        form = ManagerForm(request.POST , request.FILES, instance=manager)
        if form.is_valid():
            form.save() 
    return render(request,'management/managerProfile.html',{'form':form}) 



def profile(request):   
    group =  request.user.groups.all()[0].name
    print(group)
    if group == 'customer':
       return redirect('customerProfile')
    if group == 'manager' or group=='admin':
       return redirect('managerProfile')

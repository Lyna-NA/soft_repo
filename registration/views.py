from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
# from .forms import CreateNewUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .decorators import notLoggedUsers , allowedUsers#, formanagements
from django.contrib.auth.models import Group
from validate_email import validate_email 

# @notLoggedUsers
# def register(request):   
#     form = CreateNewUser()
#     if request.method == 'POST': 
#         form = CreateNewUser(request.POST)
#         if form.is_valid():
#             user=form.save()
#             username=form.cleaned_data.get('username')
#             group =Group.objects.get(name='customer')
#             user.groups.add(group)            
#             messages.success(request , username + ' Created Successfully !')
#             return redirect('login')
#         else:
#             messages.error(request ,  ' invalid Recaptcha please try again!')  

#     context = {'form':form}
#     return render(request , 'registration/auth/register.html', context )


# @notLoggedUsers
# def loginView(request):  
 
#     if request.method == 'POST': 
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request , username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Credentials error')

#     context = {}

#     return render(request , 'registration/auth/login.html', context )


@notLoggedUsers
def signup(request):

    if request.method == 'GET': 
        return render (request , 'registration/auth/signup.html')

    if request.method == 'POST': 
        context = {
        'data' : request.POST,
        'has_error':False
        }
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not validate_email(email):
            messages.add_message(request,messages.ERROR,'please provide valid email')
            context ['has_error']=True

        if len(password)<8:
            messages.add_message(request,messages.ERROR,'your password less than 8 character')
            context ['has_error']=True

        if password != password2:
            messages.add_message(request,messages.ERROR,'your passwords does not match  ')
            context ['has_error']=True
        try:

           if User.objects.get(email=email):

               messages.add_message(request,messages.ERROR,'email is taken ')
               context ['has_error']=True

        except Exception as identifier:
            pass

        try:

           if User.objects.get(username=username):

               messages.add_message(request,messages.ERROR,'username is taken ')
               context ['has_error']=True
        except Exception as identifier:
            pass
        
        if context ['has_error']:

            return render (request , 'registration/auth/signup.html',context)

        user =User.objects.create_user(username=username,email=email)
        user.set_password(password)
        user.is_active = True
        group =Group.objects.get(name='customer')
        user.groups.add(group)         
        user.save()
        
        messages.add_message(request,messages.SUCCESS,'user is created ')
        con ={
            'username':get_object_or_404(User,username =username),
        }

        login(request, user)
        return redirect('setInfo')

#****************************************************************************
@notLoggedUsers
def signin(request):

    if request.method == 'GET': 
        return render(request, 'registration/auth/signin.html')

    if request.method == 'POST': 
        context = {
            'data': request.POST,
            'has_error': False
        }
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == '':
            messages.add_message(request, messages.ERROR,'Username is required')
            context['has_error'] = True

        if password == '':
            messages.add_message(request, messages.ERROR,'Password is required')
            context['has_error'] = True

        user = authenticate(request, username=username, password=password)

        if not user and not context['has_error']:
            messages.add_message(request, messages.ERROR, 'Invalid login')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'registration/auth/signin.html', status=401, context=context)

        login(request, user)
        return redirect('home')


def userLogout(request):  
    logout(request)
    return redirect('signin') 


@allowedUsers('customer')
def setInfo(request):
    if request.method =="GET":
        return render (request , 'registration/auth/setInfo.html')

    if request.method =="POST":
        context = {
        'data' : request.POST,
        'has_error':False
        }
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender =request.POST.get('gender')
        country =request.POST.get('country')
        city =request.POST.get('city')
        state =request.POST.get('state')
        street =request.POST.get('street')
        building_num =request.POST.get('building_num')
        dept_num =request.POST.get('dept_num')
        
        
        user =get_object_or_404(User,username=username)
        user.first_name=first_name
        user.last_name=last_name
        user.gender=gender
        user.country=country
        user.city=city
        user.state=state
        user.street=street
        user.building_num= building_num
        user.dept_num=dept_num
        
        user.save()
        
        messages.add_message(request,messages.SUCCESS,'Added successfully')
        

        return redirect('user_dashboard')
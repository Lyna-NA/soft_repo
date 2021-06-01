from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import CreateNewUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .decorators import notLoggedUsers , allowedUsers#, formanagements
from django.contrib.auth.models import Group



# class RegisterationView(View):
    
#     def get( self , request):
#         return render (request , 'registration/auth/register.html')
#     def post( self , request):
#         context = {
#         'data' : request.POST,
#         'has_error':False
#         }

#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password2 = request.POST.get('password2')

#         # if not validate_email(email):
#         #     messages.add_message(request,messages.ERROR,'please provide valid email ')
#         #     context ['has_error']=True

#         if len(password)<8:
#             messages.add_message(request,messages.ERROR,'your password less than 8 character  ')
#             context ['has_error']=True

#         if password != password2:
#             messages.add_message(request,messages.ERROR,'your passwords does not match  ')
#             context ['has_error']=True
#         try:

#            if User.objects.get(email=email):

#                messages.add_message(request,messages.ERROR,'email is taken ')
#                context ['has_error']=True
#         except Exception as identifier:
#             pass

#         try:

#            if User.objects.get(username=username):
#                messages.add_message(request,messages.ERROR,'username is taken ')
#                context ['has_error']=True
#         except Exception as identifier:
#             pass
        
#         if context ['has_error']:

#             return render (request , 'registration/auth/register.html',context)

#         user =User.objects.create_user(username=username,email=email)
#         user.set_password(password)
#         user.is_active = False
#         user.save()

#         messages.add_message(request,messages.SUCCESS,'user is created ')
#         return redirect('register')


# class loginView(View):
#     def get(self, request):
#         return render(request, 'registration/auth/login.html')

#     def post(self, request):
#         context = {
#             'data': request.POST,
#             'has_error': False
#         }
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         if username == '':
#             messages.add_message(request, messages.ERROR,
#                                  'Username is required')
#             context['has_error'] = True
#         if password == '':
#             messages.add_message(request, messages.ERROR,
#                                  'Password is required')
#             context['has_error'] = True
#         user = authenticate(request, username=username, password=password)

#         if  user :
#             messages.add_message(request, messages.ERROR, 'Invalid login')
#             context['has_error'] = True

#         if context['has_error']:
#             return render(request, 'registration/auth/login.html', status=401, context=context)
#         login(request, user)
        
#         return redirect('home')

@notLoggedUsers
def register(request):   
    form = CreateNewUser()
    if request.method == 'POST': 
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group =Group.objects.get(name='customer')
            user.groups.add(group)            
            messages.success(request , username + ' Created Successfully !')
            return redirect('login')
        else:
            messages.error(request ,  ' invalid Recaptcha please try again!')  

    context = {'form':form}
    return render(request , 'registration/auth/register.html', context )


@notLoggedUsers
def loginView(request):  
 
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials error')

    context = {}

    return render(request , 'registration/auth/login.html', context )


def userLogout(request):  
    logout(request)
    return redirect('login') 


# @login_required(login_url='login')
# #@allowedUsers(allowedGroups=['customer'])
# def userProfile(request):  
     
#     orders = request.user.customer.order_set.all()

#     t_orders = orders.count()
#     p_orders = orders.filter(status='Pending').count()
#     d_orders = orders.filter(status='Delivered').count()
#     in_orders = orders.filter(status='in progress').count()
#     out_orders = orders.filter(status='out of order').count()
#     context = { 
#                'orders': orders,
#                't_orders': t_orders,
#                'p_orders': p_orders,
#                'd_orders': d_orders,
#                'in_orders': in_orders,
#                'out_orders': out_orders}

    
#     return render(request , 'bookstore/profile.html', context )

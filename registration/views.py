from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login  , logout 
from django.contrib.auth.decorators import  login_required
#from .decorators import notLoggedUsers , allowedUsers, formanagements
from django.contrib.auth.models import Group

# Create your views here.

##########################################################################################################3
# auth 
#@notLoggedUsers
# def register(request):   
#             form = CreateNewUser()
#             if request.method == 'POST': 
#                    form = CreateNewUser(request.POST)
#                    if form.is_valid():

#                        recaptcha_response = request.POST.get('g-recaptcha-response')
#                        data = {
#                            'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
#                            'response' : recaptcha_response
#                        }
#                        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
#                        result = r.json()
#                        if result['success']:
#                            user = form.save()
#                            username = form.cleaned_data.get('username')
#                            messages.success(request , username + ' Created Successfully !')
#                            return redirect('login')
#                        else:
#                           messages.error(request ,  ' invalid Recaptcha please try again!')  
 
        
#             context = {'form':form}

#             return render(request , 'bookstore/register.html', context )

def userLogin(request):  
 
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

#@notLoggedUsers
# def userLogin(request):  
    
#     def get(self, request):
#         return render(request, 'authentication/auth/login.html')

#     def post(self, request):
#         context = {
#             'data': request.POST,
#             'has_error': False
#         }
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         if username == '':
#             messages.add_message(request, messages.ERROR,'Username is required')
#             context['has_error'] = True

#         if password == '':
#             messages.add_message(request, messages.ERROR,'Password is required')
#             context['has_error'] = True

#         user = authenticate(request, username=username, password=password)

#         if not user : #not registered one
#             messages.add_message(request, messages.ERROR, 'Invalid login')
#             context['has_error'] = True

#         if context['has_error']:
#             return render(request, 'authentication/auth/login.html', status=401, context=context)

#         login(request, user)
#         return redirect('home')


# def userLogout(request):  
#     logout(request)
#     return redirect('login') 


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

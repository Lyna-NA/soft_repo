from django.shortcuts import render
from django.views.generic import View

# Create your views here.

def user_dashboard(request):
    if request.method == 'GET': 
        return render(request ,'userSide/user_dashboard.html')
        
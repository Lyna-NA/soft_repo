from django.urls import path
from . import views

urlpatterns = [
    # auth app 
    path('signup/' ,views.signup, name="signup"),
    path('signin/' ,views.signin, name="signin"),
    path('logout/' ,views.userLogout, name="logout"),
    path('setInfo/' ,views.setInfo, name="setInfo"),

]
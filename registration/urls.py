from django.urls import path
from . import views

urlpatterns = [
    # auth app 
    # path('register/' ,views.register, name="register"),
    path('login/' ,views.userLogin, name="login"),
    # path('logout/' ,views.userLogout, name="logout"),
]
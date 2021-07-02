from django.urls import path
from . import views

urlpatterns = [
     path('user_dashboard',  views.user_dashboard,  name = 'user_dashboard'),
     path('index',  views.index,  name = 'index'),
     path('books'  ,  views.books   ,  name = 'books'),
     path('books2'  ,  views.books2   ,  name = 'books2'),
     path('bookInfo/<int:book_id>/',  views.bookInfo ,  name='bookInfo'),
     path('bookInfo2/<int:book_id>/',  views.bookInfo2 ,  name='bookInfo2'),
     path('issues/<str:username>/',  views.issue ,  name='issue'),
     path('notReturned/<str:username>/',  views.notReturned ,  name='notReturned'),
     path('logoutCustomer',  views.logoutCustomer ,  name='logoutCustomer'),


]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('errorPage/',views.errorPage),
    path('addBook/',views.addBook),
    path('addCat/',views.addCat),
    path('addShelf/',views.addShelf),
    path('blank/',views.blank),
    path('booksList/',views.booksList),
    path('catList/',views.catList),
    path('createIssue/',views.createIssue),
    path('forgot_password/',views.forgot_password),
    path('issuesList/',views.issuesList),
    path('login/',views.login),
    path('non_returnedBooks/',views.non_returnedBooks),
    path('profile/',views.profile),
    path('register/',views.register),
    path('table/',views.table),
]

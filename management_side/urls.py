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
    path('profileManager/',views.profileManager),
#    path('profileMember/',views.profileMember),
    path('profileMember/<str:pk>/',views.profileMember),
    path('register/',views.register),
    path('membersList/',views.membersList),
    path('managersList/',views.managersList),
    path('addUser/',views.addUser),
]

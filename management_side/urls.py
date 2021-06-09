from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('manager_dashboard',views.manager_dashboard,name="manager_dashboard"),
    path('errorPage/',views.errorPage,name="errorPage"),
    path('addBook/',views.addBook,name="addBook"),
    path('addCat/',views.addCat,name="addCat"),
    # path('addShelf/',views.addShelf,name="addShelf"),
    path('deleteIssue/<str:pk>/',views.deleteIssue,name="deleteIssue"),
    path('blank/',views.blank,name="blank"),
    path('booksList/',views.booksList,name="booksList"),
    path('catList/',views.catList,name="catList"),
    path('createIssue/',views.createIssue,name="createIssue"),
    path('updateIssue/<str:pk>/',views.updateIssue,name="updateIssue"),
    path('forgot_password/',views.forgot_password,name="forgot_password"),
    path('issuesList/',views.issuesList,name="issuesList"),
    path('managersList/',views.managersList,name="managersList"),
    path('non_returnedBooks/',views.non_returnedBooks,name="non_returnedBooks"),
    path('managerProfile/',views.managerProfile,name="managerProfile"),
#    path('profileMember/',views.profileMember),
    path('customerProfile/',views.customerProfile,name="customerProfile"),
    path('profile/',views.profile,name="profile"),
    path('customersList/',views.customersList,name="customersList"),
    path('managersList/',views.managersList,name="managersList"),
    path('addUser/',views.addUser,name="addUser"),
]

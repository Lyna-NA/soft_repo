from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # auth app 
    path('signup/' ,views.signup, name="signup"),
    path('signin/' ,views.signin, name="signin"),
    path('logout/' ,views.userLogout, name="logout"),
    path('setInfo/' ,views.setInfo, name="setInfo"),

]

urlpatterns +=static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)
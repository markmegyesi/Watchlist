
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import home,watched,mark_as_watched
from user_registration.views import SignUpView

urlpatterns = [
    path('',home,name='list_home'),
    path('watched/',watched,name='list_watched'),
    path('mark_as_watched/<int:id>', mark_as_watched, name='mark_as_watched'),
    path('login/', auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="user/logout.html"), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),    
]
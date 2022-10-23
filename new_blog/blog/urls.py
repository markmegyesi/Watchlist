
from django.contrib import admin
from django.urls import path
from .views import home,watched,mark_as_watched

urlpatterns = [
    path('',home,name='blog_home'),
    path('watched/',watched,name='blog_watched'),
    path('mark_as_watched/<int:id>', mark_as_watched, name='mark_as_watched')
    
]
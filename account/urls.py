"""
this urls is just for account
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import *
from .views import register
    
urlpatterns = [
 url(r'^$',detail,name='details'),
 url(r'^login',forlogin,name='forlogin'),
 url(r'^logout',forlogout,name='forlogout'),
 url(r'^register',register,name='register'),
]

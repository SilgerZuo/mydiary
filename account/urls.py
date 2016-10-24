"""
this urls is just for account
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import *
from .views import regist
    
urlpatterns = [
 url(r'^$',detail,name='details'),
 url(r'^login',forlogin,name='forlogin'),
 url(r'^logout',forlogout,name='forlogout'),
 url(r'^regist',regist,name=regist),
]

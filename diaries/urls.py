from django.conf.urls import include, url
from django.contrib import admin
from account.account_urls import *
from django.contrib.auth import views as auth_views
from .views import homepage
from .views import all_dry
from .views import diary_detail
urlpatterns = [
    url(r'^$', homepage, name='home'),
    url(r'^login',auth_views.login,name='loginfordry'),
    url(r'^all',all_dry,name='alldiaries'),
    url(r'^diarypage',all_dry,name='diarypage'),
    url(r'^detail/(?P<diary_id>[0-9]+)/$',diary_detail,name='diary_detail')
]

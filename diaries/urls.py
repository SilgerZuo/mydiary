from django.conf.urls import include, url
from django.contrib import admin
from account.account_urls import *
from django.contrib.auth import views as auth_views
from .views import homepage
from .views import all_dry
from .views import diary_detail
from .views import mydiary
urlpatterns = [
    url(r'^$', homepage, name='home'),
    url(r'^login',auth_views.login,name='login'),
    url(r'^logout',auth_views.logout,name='logoutfordry'),
    url(r'^all',homepage,name='alldiaries'),
    url(r'^mydiary',mydiary,name='mydiary'),
    url(r'^new_diary',mydiary,name='new_diary'),
    url(r'^detail/(?P<diary_id>[0-9]+)/$',diary_detail,name='diary_detail')
]

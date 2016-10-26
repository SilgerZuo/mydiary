#*-encoding:utf-8-*
from django.shortcuts import render,Http404,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from diaries.views import homepage
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
# class UserForm(forms.Form):
from django.http import HttpResponseRedirect
from .models import Diaryuser
from django.contrib.auth.models import User



def detail(request):
    return render(request,'account/regist_page.html',None)


def forlogin(request):
    try:
        username=request.REQUEST.get('username','noname')
        password=request.REQUEST.get('password','nopass')
    except:
        raise Http404
    user=authenticate(username=username,password=password)
    if(user):
        login(request,user)
            # return render(request,'diaries/all_dry.html')
        return HttpResponseRedirect('/diary')
    else:
        return render(request,'account/login_fail.html')




def forlogout(request):
    logout(request)
    # return render(request, 'diaries/all_dry.html')
    return HttpResponseRedirect('/diary')


def register(request):
    try:
        username=request.POST.get("register-name",None)
        password=request.POST.get('register-password-1')
        email=request.POST.get("register-email",None)
    except:
        raise Http404
    name_registered = 0;
    email_registered = 0;
    if(len(User.objects.filter(username=username))>0):
        name_registered=1;
    if(len(User.objects.filter(username=username))>0):
        email_registered=1;
    registered=email_registered+name_registered
    if((registered)>0):
        return render(request, "account/been_registered.html",{'name_registered':u"用户名已经注册",
                                                          'email_registered':u"邮箱已经注册",
                                                          'registered':registered,
                                                          })
    else:
        user = User()
        user.username = username
        user.set_password(password)
        user.email = email
        user.save()
        dryuser=Diaryuser()
        dryuser.user=user
        dryuser.save()
        return render(request,"account/registered.html",{"register_succ":u"注册成功,请登录"})

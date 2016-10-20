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


def detail(request):
    return render(request,'account/hello.html',None)


def forlogin(request):
    try:
        username=request.REQUEST.get('username','noname')
        password=request.REQUEST.get('password','nopass')
    except:
        raise Http404
    user=authenticate(username=username,password=password)
    if user.is_active:
        login(request,user)
        # return render(request,'diaries/all_dry.html')
        return HttpResponseRedirect('/diary')
    else:
        # return render(request,'diaries/all_dry.html')
        return HttpResponseRedirect('/diary')

def forlogout(request):
    logout(request)
    # return render(request, 'diaries/all_dry.html')
    return HttpResponseRedirect('/diary')

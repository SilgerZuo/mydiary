#!-*encoding:utf-8*-
from django.shortcuts import render
from diaries.models import Diary
from intrest.models import Public_intrest
from intrest.models import Person_intrest
from django.contrib.auth.models import User
from account.models import Diaryuser
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.shortcuts import get_object_or_404,Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import diaryform
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def all_dry(request):
    return render(request,'hello',None)


def homepage(request):
    diaries=Diary.objects.filter(Diary_share='Public').\
        order_by('-create_date')
    pub_intrest=Public_intrest.objects.all()
    user=request.user.username;
    try:
        per_intrest=Person_intrest.objects.\
            filter(likes_by__user__username=user)
    except:
        per_intrest=None
    page_show=Paginator(diaries,6)
    page_list=Paginator(diaries,12)
    page_num=request.GET.get('page')
    try:
        diaries=page_show.page(page_num)
        list_num=(int(page_num)/2)
        diaries_list=page_list.page(list_num)
    except PageNotAnInteger:
        diaries=page_show.page(1)
        diaries_list = page_list.page(1)
    except EmptyPage:
        diaries=page_show.page(1)
        diaries_list=page_list.page(page_list.num_pages)
    return render(request,'diaries/all_dry.html',
                  {'pub_like':pub_intrest,
                   'per_like':per_intrest,
                   'diaries':diaries,
                   'diaries_list':diaries_list,
                   })

#与homepage相似,但是完成内容不同
def diary_detail(request,diary_id):
    diary=get_object_or_404(Diary,diary_sortid=diary_id)
    req_dry_user=diary.user
    user=request.user.username;
    diaries=Diary.objects.\
        filter(Q(Diary_share='Public' )&Q(user=req_dry_user)).\
        order_by('create_date')
    pub_intrest=Public_intrest.objects.all()
    user=request.user.username;
    diary_like=get_object_or_404(Diary,diary_sortid=diary_id)
    diary_pub_like=diary_like.Person_intrest.all()
    diary_per_like=diary_like.Public_intrest.all()
    try:
        per_intrest=Person_intrest.objects.\
            filter(likes_by__user__username=user)
    except:
        per_intrest=None
    page_list=Paginator(diaries,12)
    page_num=request.GET.get('page')
    try:
        diaries=page_list.page(page_num)
        list_num=(int(page_num)/2)
        diaries_list=page_list.page(list_num)
    except PageNotAnInteger:
        diaries_list = page_list.page(1)
    except EmptyPage:
        diaries_list=page_list.page(page_list.num_pages)
    return render(request,'diaries/diarypage.html',
                  {'pub_like':diary_pub_like,
                   'per_like':diary_per_like,
                   'diaries_list':diaries_list,
                   'diary':diary,
                   })

@login_required()
def mydiary(request):
    user1 = User.objects.filter(username=request.user.username)[0]
    whoiam = Diaryuser.objects.filter(user=user1)[0]
    diaries_list = Diary.objects.filter(user=whoiam)
    if(request.method=='POST'):
        form=diaryform(request.POST)
        if form.is_valid():
            diary_title=form.cleaned_data['diary_title']
            diary_text=form.cleaned_data['diary_text']
            newdry=Diary()
            newdry.user=whoiam
            newdry.diary_title = diary_title
            newdry.diary_text = diary_text
            newdry.create_date=timezone.now()
            newdry.save()
            return HttpResponseRedirect("/diary")
        else:
            newform = diaryform()
            diaries_list = Diary.objects.filter(user=whoiam)
            return render(request, 'diaries/userpage.html',
                          {'form': newform,
                           "diaries_list":diaries_list
                           })
    else:
        form=diaryform()
        return render(request,'diaries/userpage.html',
                      {'form':form,"diaries_list":diaries_list})
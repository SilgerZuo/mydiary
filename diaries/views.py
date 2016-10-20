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
from django.core.urlresolvers import reverse
# Create your views here.
# def homepage(request):
#     return render(request,'diaries/diaries_base.html',None)
# def login(request):
#     return render(request,reverse("diarise:login"))
# @login_required
def all_dry(request):
    return render(request,'hello',None)


def homepage(request):
    diaries=Diary.objects.filter(Diary_share='Public').order_by('create_date')
    pub_intrest=Public_intrest.objects.all()
    user=request.user.username;
    try:
        per_intrest=Person_intrest.objects.filter(likes_by__user__username=user)
    except:
        per_intrest=None
    page_show=Paginator(diaries,10)
    page_list=Paginator(diaries,20)
    page_num=request.GET.get('page')
    try:
        diaries=page_show.page(page_num)
        diaries_list=page_list.page(page_num)
    except PageNotAnInteger:
        diaries=page_show.page(1)
        diaries_list = page_list.page(1)
    return render(request,'diaries/all_dry.html',
                  {'pub_like':pub_intrest,
                   'per_like':per_intrest,
                   'diaries':diaries,
                   'diaries_list':diaries_list,
                   })
def useradd(request):
    dryuser=Diary()
    username=request.Post.get('name','')
    passworc=request.Post.get('password','')
    user=User()
    user.name=username;
    Dry=Diaryuser()
    Dry.user=user;
    Dry.save()


def diary_detail(request,diary_id):
    # diary=Diary.objects.filter(diary_sortid=diary_id)
    diary=get_object_or_404(Diary,diary_sortid=diary_id)
    req_dry_user=diary.user
    user=request.user.username;
    diaries=Diary.objects.filter(Q(Diary_share='Public' )&Q(user=req_dry_user)).order_by('create_date')
    pub_intrest=Public_intrest.objects.all()
    user=request.user.username;
    diary_like=get_object_or_404(Diary,diary_sortid=diary_id)
    diary_pub_like=diary_like.Person_intrest.all()
    diary_per_like=diary_like.Public_intrest.all()
    try:
        per_intrest=Person_intrest.objects.filter(likes_by__user__username=user)
    except:
        per_intrest=None
    page_list=Paginator(diaries,20)
    page_num=request.GET.get('page')
    try:
        diaries_list=page_list.page(page_num)
    except PageNotAnInteger:
        diaries_list = page_list.page(1)
    return render(request,'diaries/diarypage.html',
                  {'pub_like':diary_pub_like,
                   'per_like':diary_per_like,
                   'diaries':diaries,
                   'diary':diary,
                   })



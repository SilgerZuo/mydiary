#*-encoding:utf-8-*
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from diaries.models import Diary
# Create your models here.
# This is the comment to dairy


class Comment(models.Model):
    Author = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=u'作者')
    comment_text = models.TextField(max_length=2000, verbose_name=u'评论')
    diary_to = models.ForeignKey(Diary, verbose_name=u'评论日记')
    c_date = models.DateTimeField(auto_now_add=True,verbose_name=u'评论时间')

    class Meta:
        verbose_name_plural = verbose_name = u'评论'
        ordering = ['-c_date']

    def __unicode__(self):
        return self.comment_text

#*-encoding:utf-8-*
from django.db import models
from intrest.models import Person_intrest, Public_intrest
from account.models import Diaryuser
# Create your models here.
share_or_not = [
    ('Public', u'公共日记'),
    ('Person', u'私密私密'),
]


class Diary(models.Model):
    # user=models.ForeignKey(settings.AUTH_USER_MODEL,
    #                        related_name='diary_written',verbose_name=u'作者')
    user = models.ForeignKey(Diaryuser, related_name='diaryuser')
    diary_text = models.TextField(
        max_length=100000, verbose_name=u'日记内容')
    diary_title = models.CharField(max_length=200, verbose_name=u'日结标题')
    diary_sortid = models.IntegerField(
        primary_key=True, db_column="DiaryId", default=1)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    likes_count = models.IntegerField(default=0, verbose_name=u'点赞数')
    # Person_intrest=models.ManyToManyField(Person_intrest,verbose_name=u'个人爱好',null=True)
    # Public_intrest=models.ManyToManyField(Public_intrest,
    #                                       verbose_name=u'公共爱好',null=True)
    Diary_share = models.CharField(
        max_length=50,
        choices=share_or_not,
        default=share_or_not[0][0],
        verbose_name=u'是否分享')

    class Meta:
        ordering = ['-create_date']
        verbose_name_plural = verbose_name = u'日记'

    def __unicode__(self):
        return self.diary_title

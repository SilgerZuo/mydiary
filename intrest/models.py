#*-encoding:utf-8-*
from django.db import models
from account.models import Diaryuser

# Create your models here.
# this is goven by administratoruser,everyone can refer
class Public_intrest(models.Model):
    pub_intrest = models.CharField(max_length=50,
                                      verbose_name=u'公共爱好')
    p_i_describe = models.TextField(max_length=2000, verbose_name=u'爱好描述',
                                    default='')
    likes_by=models.ManyToManyField(Diaryuser)
    def __unicode__(self):
        return self.pub_intrest

    class Meta:
        verbose_name_plural = verbose_name = '公共爱好'


# this is for users
class Person_intrest(models.Model):
    per_intrest = models.CharField(max_length=50,
                                      verbose_name=u'个人爱好')
    p_i_describe = models.TextField(max_length=2000, verbose_name=u'爱好描述'
                                    )
    # belong_to=models.ForeignKey(Person_intrest)
    likes_by=models.ForeignKey(Diaryuser)
    def __unicode__(self):
        return self.per_intrest

    class Meta:
        verbose_name_plural = verbose_name = '个人爱好'

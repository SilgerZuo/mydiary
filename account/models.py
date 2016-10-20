#*-encoding:utf-8-*
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from intrest.models import Public_intrest, Person_intrest
# Create your models here.


# this is the detail of the user
class Diaryuser(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL,
    #                             verbose_name=u'用户')
    user=models.OneToOneField(User)
    # public_intrest = models.ManyToManyField(Public_intrest,
    #                                         verbose_name=u'公共爱好')
    # person_intrest = models.ManyToManyField(Person_intrest,
    #                                         verbose_name=u'私人爱好')
    age = models.IntegerField(null=False, default=16,
                              verbose_name=u'年龄')
    telephone = models.CharField(max_length=11, null=True, blank=True,
                                 verbose_name=u'电话号码')
    # head = models.ImageField(upload_to='photo/')
    # background = models.ImageField(upload_to='background/')

    class Meta:
        verbose_name_plural = verbose_name = '用户'

    def __unicode__(self):
        return'{}'.format(self.user.username)


class Follow(models.Model):
    followed = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='followed',
        verbose_name=u'被关注者')
    followers = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='followers',
        verbose_name=u'关注者')
    connect = models.DateTimeField(auto_now_add=True, db_index=True,
                                   verbose_name=u'关注纽带')

    class Meta:
        ordering = ['-connect']
        verbose_name_plural = verbose_name = u'关注关系'

    def __unicode__(self):
        return "{} is following by {}".format(self.followed, self.followers)

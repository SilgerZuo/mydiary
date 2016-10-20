from django.contrib import admin
from account.models import Diaryuser
from intrest.models import Public_intrest
from intrest.models import Person_intrest
from account.models import Follow
# Register your models here.

# admin.site.register(Diaryuser)
admin.site.register(Public_intrest)
admin.site.register(Person_intrest)
admin.site.register(Diaryuser)
admin.site.register(Follow)
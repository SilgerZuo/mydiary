# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20161019_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryuser',
            name='age',
            field=models.IntegerField(default=16, null=True, verbose_name='\u5e74\u9f84'),
        ),
    ]

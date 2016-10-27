# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0013_auto_20161025_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]

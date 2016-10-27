# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0011_auto_20161025_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]

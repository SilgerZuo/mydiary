# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0004_auto_20161018_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='user',
            field=models.ForeignKey(related_name='diaryuser', to='account.Diaryuser'),
        ),
    ]

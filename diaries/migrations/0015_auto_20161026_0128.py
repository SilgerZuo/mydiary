# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0014_auto_20161025_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='diary_sortid',
            field=models.IntegerField(serialize=False, primary_key=True, db_column=b'DiaryId'),
        ),
    ]

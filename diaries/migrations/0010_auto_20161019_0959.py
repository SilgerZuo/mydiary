# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0009_auto_20161019_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='diary_sortid',
            field=models.IntegerField(default=1, serialize=False, primary_key=True, db_column=b'DiaryId'),
        ),
    ]

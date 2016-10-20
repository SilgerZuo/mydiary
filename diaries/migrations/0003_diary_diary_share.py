# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0002_auto_20161013_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='Diary_share',
            field=models.CharField(default=None, max_length=50, choices=[(b'Public', '\u516c\u5171\u65e5\u8bb0'), (b'Person', '\u79c1\u5bc6\u79c1\u5bc6')]),
        ),
    ]

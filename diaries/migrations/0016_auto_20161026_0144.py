# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0015_auto_20161026_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='Diary_share',
            field=models.CharField(default=b'Public', max_length=50, verbose_name='\u662f\u5426\u5206\u4eab', choices=[(b'Public', '\u516c\u5171\u65e5\u8bb0'), (b'Person', '\u79c1\u5bc6\u79c1\u5bc6')]),
        ),
    ]

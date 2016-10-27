# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0010_auto_20161019_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='Diary_share',
            field=models.CharField(default=(b'Person', '\u79c1\u5bc6\u79c1\u5bc6'), max_length=50, verbose_name='\u662f\u5426\u5206\u4eab', choices=[(b'Public', '\u516c\u5171\u65e5\u8bb0'), (b'Person', '\u79c1\u5bc6\u79c1\u5bc6')]),
        ),
        migrations.AlterField(
            model_name='diary',
            name='Person_intrest',
            field=models.ManyToManyField(to='intrest.Person_intrest', null=True, verbose_name='\u4e2a\u4eba\u7231\u597d'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='Public_intrest',
            field=models.ManyToManyField(to='intrest.Public_intrest', null=True, verbose_name='\u516c\u5171\u7231\u597d'),
        ),
    ]

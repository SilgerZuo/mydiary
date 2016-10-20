# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person_intrest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_intrest', models.CharField(max_length=50, verbose_name='\u4e2a\u4eba\u7231\u597d')),
                ('p_i_describe', models.TextField(max_length=2000, verbose_name='\u7231\u597d\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u4e2a\u4eba\u7231\u597d',
                'verbose_name_plural': '\u4e2a\u4eba\u7231\u597d',
            },
        ),
        migrations.CreateModel(
            name='Public_intrest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public_intrest', models.CharField(max_length=50, verbose_name='\u516c\u5171\u7231\u597d')),
                ('p_i_describe', models.TextField(default=b'', max_length=2000, verbose_name='\u7231\u597d\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u516c\u5171\u7231\u597d',
                'verbose_name_plural': '\u516c\u5171\u7231\u597d',
            },
        ),
    ]

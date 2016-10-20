# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diaries', '0002_auto_20161013_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField(max_length=2000, verbose_name='\u8bc4\u8bba')),
                ('c_date', models.DateTimeField(auto_now_add=True, verbose_name='\u8bc4\u8bba\u65f6\u95f4')),
                ('Author', models.OneToOneField(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
                ('diary_to', models.ForeignKey(verbose_name='\u8bc4\u8bba\u65e5\u8bb0', to='diaries.Diary')),
            ],
            options={
                'ordering': ['-c_date'],
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
    ]

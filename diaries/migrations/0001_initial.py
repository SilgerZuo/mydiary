# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('intrest', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diary_text', models.TextField(max_length=100000, verbose_name='\u65e5\u8bb0\u5185\u5bb9')),
                ('diary_title', models.CharField(max_length=200, verbose_name='\u65e5\u7ed3\u6807\u9898')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('likes_count', models.IntegerField(default=0)),
                ('Person_intrest', models.ForeignKey(to='intrest.Person_intrest')),
                ('Public_intrest', models.ForeignKey(to='intrest.Public_intrest')),
                ('user', models.ForeignKey(related_name='diary_written', verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_date'],
                'verbose_name': '\u65e5\u8bb0',
                'verbose_name_plural': '\u65e5\u8bb0',
            },
        ),
    ]

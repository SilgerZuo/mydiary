# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('intrest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diaryuser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(default=16, verbose_name='\u5e74\u9f84')),
                ('telephone', models.CharField(max_length=11, null=True, verbose_name='\u7535\u8bdd\u53f7\u7801', blank=True)),
                ('person_intrest', models.ManyToManyField(to='intrest.Person_intrest', verbose_name='\u79c1\u4eba\u7231\u597d')),
                ('public_intrest', models.ManyToManyField(to='intrest.Public_intrest', verbose_name='\u516c\u5171\u7231\u597d')),
                ('user', models.OneToOneField(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('connect', models.DateTimeField(auto_now_add=True, verbose_name='\u5173\u6ce8\u7ebd\u5e26', db_index=True)),
                ('followed', models.OneToOneField(related_name='followed', verbose_name='\u88ab\u5173\u6ce8\u8005', to=settings.AUTH_USER_MODEL)),
                ('followers', models.OneToOneField(related_name='followers', verbose_name='\u5173\u6ce8\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-connect'],
                'verbose_name': '\u5173\u6ce8\u5173\u7cfb',
                'verbose_name_plural': '\u5173\u6ce8\u5173\u7cfb',
            },
        ),
    ]

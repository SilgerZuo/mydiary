# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intrest', '0001_initial'),
        ('diaries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='Person_intrest',
        ),
        migrations.AddField(
            model_name='diary',
            name='Person_intrest',
            field=models.ManyToManyField(to='intrest.Person_intrest'),
        ),
        migrations.RemoveField(
            model_name='diary',
            name='Public_intrest',
        ),
        migrations.AddField(
            model_name='diary',
            name='Public_intrest',
            field=models.ManyToManyField(to='intrest.Public_intrest'),
        ),
    ]

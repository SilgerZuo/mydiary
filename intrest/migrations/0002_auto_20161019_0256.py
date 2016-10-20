# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20161019_0256'),
        ('intrest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person_intrest',
            old_name='person_intrest',
            new_name='per_intrest',
        ),
        migrations.RenameField(
            model_name='public_intrest',
            old_name='public_intrest',
            new_name='pub_intrest',
        ),
        migrations.AddField(
            model_name='person_intrest',
            name='likes_by',
            field=models.ForeignKey(default=2, to='account.Diaryuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='public_intrest',
            name='likes_by',
            field=models.ManyToManyField(to='account.Diaryuser'),
        ),
    ]

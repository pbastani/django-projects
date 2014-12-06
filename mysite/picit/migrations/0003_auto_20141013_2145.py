# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picit', '0002_auto_20141013_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='image',
            name='pic_date',
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.CharField(default='', max_length=500),
            preserve_default=True,
        ),
    ]

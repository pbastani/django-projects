# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0007_auto_20141021_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='iconUrl',
            field=models.CharField(max_length=1000, default='', verbose_name='Icon URL'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200, default='', verbose_name='Title'),
        ),
    ]

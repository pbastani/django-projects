# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0006_auto_20141021_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='Description', default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='referenceUrl',
            field=models.CharField(verbose_name='Reference URL', max_length=1000, default=''),
        ),
    ]

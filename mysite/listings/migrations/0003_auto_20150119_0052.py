# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_post_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.date(2000, 1, 1)),
        ),
        migrations.AlterField(
            model_name='post',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.date(2000, 1, 1)),
        ),
    ]

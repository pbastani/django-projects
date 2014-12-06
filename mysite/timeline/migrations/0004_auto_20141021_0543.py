# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0003_event_iconurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='referenceUrl',
        ),
        migrations.AddField(
            model_name='event',
            name='Reference',
            field=models.CharField(default='', max_length=1000),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_auto_20141021_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='iconUrl',
            field=models.CharField(max_length=1000, default=''),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picit', '0006_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
    ]

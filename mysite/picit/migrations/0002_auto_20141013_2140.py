# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='img_url',
            new_name='image_url',
        ),
    ]

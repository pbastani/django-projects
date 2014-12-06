# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_auto_20141021_0543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Reference',
            new_name='referenceUrl',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0008_auto_20141021_0547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='iconUrl',
            new_name='icon_url',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='referenceUrl',
            new_name='reference_url',
        ),
    ]

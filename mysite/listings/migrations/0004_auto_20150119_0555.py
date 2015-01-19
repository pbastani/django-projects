# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20150119_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=2, choices=[(None, 'Select a category'), ('general', 'General'), ('forsale', 'For Sale'), ('services', 'Services'), ('housing', 'Housing')], default='general'),
        ),
    ]

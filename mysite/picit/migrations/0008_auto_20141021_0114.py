# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picit', '0007_remove_image_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=models.ForeignKey(related_name='tags', to='picit.Image'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20150119_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('post_id', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(to='listings.Profile', related_name='favorites')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

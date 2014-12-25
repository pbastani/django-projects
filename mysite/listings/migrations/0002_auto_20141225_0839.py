# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('file', models.ImageField(upload_to='listing_images/%Y/%m/%d', default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', default='', max_length=200)),
                ('content', models.CharField(verbose_name='Content', default='', max_length=10000)),
                ('create_date', models.DateField(verbose_name='Posted On')),
                ('views', models.IntegerField(default=0)),
                ('user', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='picture',
            name='post',
            field=models.ForeignKey(related_name='pictures', to='listings.Post'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_online',
            field=models.DateTimeField(default=datetime.date(2014, 12, 25)),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('file', models.ImageField(upload_to='listing_images/%Y/%m/%d', default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, default='')),
                ('content', models.CharField(max_length=10000, default='')),
                ('create_date', models.DateField(default=datetime.date(2000, 1, 1))),
                ('expiry_date', models.DateField(default=datetime.date(2000, 1, 1))),
                ('views', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=50, default='')),
                ('price', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=2, choices=[(None, 'Select a category'), ('GN', 'General'), ('FS', 'For Sale'), ('SV', 'Services'), ('HS', 'Housing')], default='GN')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='posts')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('last_online', models.DateTimeField(default=datetime.date(2000, 1, 1))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50, verbose_name='Tag', default='')),
                ('posts', models.ManyToManyField(to='listings.Post', related_name='tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='picture',
            name='post',
            field=models.ForeignKey(to='listings.Post', related_name='pictures'),
            preserve_default=True,
        ),
    ]

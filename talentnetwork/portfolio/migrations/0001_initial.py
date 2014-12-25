# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('text', models.CharField(default='', verbose_name='Comment', max_length=1000)),
                ('post_date', models.DateField(verbose_name='Posted On')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('file', models.FileField(default='', upload_to='portfolio_images/')),
                ('views', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=50)),
                ('upload_date', models.DateField(verbose_name='Uploaded On')),
                ('position', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='photos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('aboutme', models.TextField(verbose_name='Intro', null=True)),
                ('website_url', models.URLField(verbose_name='Website URL', null=True)),
                ('website_name', models.CharField(verbose_name='Website Name', null=True, max_length=50)),
                ('picture', sorl.thumbnail.fields.ImageField(null=True, upload_to='profile_images/%Y/%m/%d')),
                ('last_online', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 1, 1, 1, 1))),
                ('followee', models.ManyToManyField(to='portfolio.Profile', related_name='followees')),
                ('follower', models.ManyToManyField(to='portfolio.Profile', related_name='followers')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(to='portfolio.Photo', related_name='comments'),
            preserve_default=True,
        ),
    ]

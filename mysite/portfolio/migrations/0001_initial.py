# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('aboutme', models.TextField(null=True, verbose_name='Intro')),
                ('website_url', models.URLField(null=True, verbose_name='Website URL')),
                ('website_name', models.CharField(null=True, verbose_name='Website Name', max_length=50)),
                ('picture', models.FileField(null=True, upload_to='profile_images/%Y/%m/%d')),
                ('last_online', models.DateTimeField(default=datetime.date(2014, 12, 19))),
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

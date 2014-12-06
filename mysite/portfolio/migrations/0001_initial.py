# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.CharField(verbose_name='Comment', max_length=1000, default='')),
                ('post_date', models.DateField(verbose_name='Posted On')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('file', models.FileField(default='', upload_to='portfolio_images/')),
                ('views', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=50, default='')),
                ('upload_date', models.DateField(verbose_name='Uploaded On')),
                ('position', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('aboutme', models.TextField(verbose_name='Intro', null=True)),
                ('website_url', models.URLField(verbose_name='Website URL', null=True)),
                ('website_name', models.CharField(verbose_name='Website Name', null=True, max_length=50)),
                ('picture', models.FileField(null=True, upload_to='profile_images/%Y/%m/%d')),
                ('user', models.ForeignKey(related_name='profile', unique=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photo',
            name='profile',
            field=models.ForeignKey(related_name='photos', to='portfolio.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(related_name='comments', to='portfolio.Photo'),
            preserve_default=True,
        ),
    ]

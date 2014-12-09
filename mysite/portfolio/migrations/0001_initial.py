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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=1000, verbose_name='Comment')),
                ('post_date', models.DateField(verbose_name='Posted On')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('me', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('file', models.FileField(default='', upload_to='portfolio_images/')),
                ('views', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=50)),
                ('upload_date', models.DateField(verbose_name='Uploaded On')),
                ('position', models.IntegerField(default=0)),
                ('user', models.ForeignKey(related_name='photos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('aboutme', models.TextField(null=True, verbose_name='Intro')),
                ('website_url', models.URLField(null=True, verbose_name='Website URL')),
                ('website_name', models.CharField(null=True, max_length=50, verbose_name='Website Name')),
                ('picture', models.FileField(null=True, upload_to='profile_images/%Y/%m/%d')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(related_name='comments', to='portfolio.Photo'),
            preserve_default=True,
        ),
    ]

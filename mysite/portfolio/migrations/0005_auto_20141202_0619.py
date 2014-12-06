# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0004_auto_20141202_0543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aboutme', models.TextField(verbose_name='Intro', null=True)),
                ('website_url', models.URLField(verbose_name='Website URL', null=True)),
                ('website_name', models.CharField(max_length=50, verbose_name='Website Name', null=True)),
                ('picture', models.FileField(upload_to='profile_images/%Y/%m/%d', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AlterField(
            model_name='photo',
            name='profile',
            field=models.ForeignKey(to='portfolio.Profile', related_name='photos'),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]

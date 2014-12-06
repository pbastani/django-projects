# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0003_auto_20141202_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('aboutme', models.TextField(null=True, verbose_name='Intro')),
                ('website_url', models.URLField(null=True, verbose_name='Website URL')),
                ('website_name', models.CharField(null=True, max_length=50, verbose_name='Website Name')),
                ('picture', models.FileField(upload_to='profile_images/%Y/%m/%d', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='photo',
            name='profile',
            field=models.ForeignKey(related_name='photos', to='portfolio.Account'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

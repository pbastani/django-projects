from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
import datetime
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    aboutme = models.TextField("Intro", null=True)
    website_url = models.URLField("Website URL", null=True)
    website_name = models.CharField("Website Name", max_length=50, null=True)
    picture = ImageField(upload_to='profile_images/%Y/%m/%d', null=True)
    last_online = models.DateTimeField(default=datetime.datetime(1970, 1, 1, 1, 1, 1, 1, tzinfo=None))
    follower = models.ManyToManyField("self", related_name='followers', symmetrical=False)
    followee = models.ManyToManyField("self", related_name='followees', symmetrical=False)

    def __str__(self):
        return self.user.username


class Photo(models.Model):
    user = models.ForeignKey(User, related_name='photos')
    file = models.ImageField(upload_to='portfolio_images/%Y/%m/%d', default="")
    views = models.IntegerField(default=0)
    title = models.CharField(max_length=50, default="")
    upload_date = models.DateField('Uploaded On')
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    photo = models.ForeignKey(Photo, related_name='comments')
    text = models.CharField("Comment", max_length=1000, default="")
    post_date = models.DateField('Posted On')

    def __str__(self):
        return self.text
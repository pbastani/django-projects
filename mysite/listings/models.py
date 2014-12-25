from django.db import models
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    last_online = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    title = models.CharField("Title", max_length=200, default="")
    content = models.CharField("Content", max_length=10000, default="")
    create_date = models.DateField('Posted On')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Picture(models.Model):
    post = models.ForeignKey(Post, related_name='pictures')
    file = models.ImageField(upload_to='listing_images/%Y/%m/%d', default="")

    def __str__(self):
        return self.file.url
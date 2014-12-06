from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    # user = models.ForeignKey(User, unique=True, related_name='profile')
    aboutme = models.TextField("Intro", null=True)
    website_url = models.URLField("Website URL", null=True)
    website_name = models.CharField("Website Name", max_length=50, null=True)
    picture = models.FileField(upload_to='profile_images/%Y/%m/%d', null=True)

    def __str__(self):
        return self.user.username


#class Portfolio(models.Model):
    # user = models.OneToOneField(User, primary_key=True, related_name='portfolio')
#    user = models.OneToOneField(User)
    # user = models.ForeignKey(User, unique=True, related_name='portfolio')
#    name = models.CharField("Name", max_length=100, default="")
#    def __str__(self):
#        return self.user.username


class Photo(models.Model):
    profile = models.ForeignKey(Profile, related_name='photos')
    file = models.FileField(upload_to='portfolio_images/', default="")
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
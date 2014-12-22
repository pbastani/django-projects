from django.db import models
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    last_online = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.username
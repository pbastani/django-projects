from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100, default="")
    url = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.title


class Tag(models.Model):
    image = models.ForeignKey(Image, related_name='tags')
    text = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.text
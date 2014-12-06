from django.db import models


class Event(models.Model):
    title = models.CharField("Title", max_length=200, default="")
    description = models.TextField("Description", max_length=300, default="")
    reference_url = models.CharField("Reference URL", max_length=1000, default="")
    icon_url = models.CharField("Icon URL", max_length=1000, default="")
    date = models.DateField('Occured On')

    def __str__(self):
        return self.title


class Tag(models.Model):
    event = models.ForeignKey(Event, related_name='tags')
    text = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.text


class Category(models.Model):
    event = models.ForeignKey(Event, related_name='categories')
    text = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.text
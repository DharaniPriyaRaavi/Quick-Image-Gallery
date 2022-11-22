from django.db import models
# Create your models here.
import datetime
import os
from django.urls import reverse


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Item(models.Model):
    name = models.TextField(max_length=191)
    price = models.TextField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)

    tags = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)

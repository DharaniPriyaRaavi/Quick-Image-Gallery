
# Create your models here.
import os

from django.db import models
import datetime
from django.contrib.auth.models import User



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


class Member(User):
    Username = models.CharField(max_length=300, blank=False, default="Test")
    Email = models.CharField(max_length=300, blank=True)
    Password = models.CharField(max_length=300, blank=False,default="Test@123")
    Password_confirmation = models.CharField(max_length=300, blank=False,default="Test@123")
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, default='ON')
    picture = models.ImageField(
        upload_to='static/profileimg',
        blank=True, null=True
    )
    def __str__(self):
        return self.username


from django.conf import settings
from django.db import models

# Create your models here.

class media(models.Model):
    username = models.CharField(max_length=100, default="")
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')
    img3 = models.ImageField(upload_to='images')
    img4 = models.ImageField(upload_to='images')
    img5 = models.ImageField(upload_to='images')
    text1 = models.TextField(default="")
    text2 = models.TextField(default="")
    text3 = models.TextField(default="")
    text4 = models.TextField(default="")
    text5 = models.TextField(default="")
    lattitude = models.TextField()
    longitude = models.TextField()
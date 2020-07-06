from django.db import models
from django.contrib.auth.models import User as UserBase


class User(UserBase):
    phone = models.CharField(max_length=32)


class Offer(models.Model):
    image = models.FileField(upload_to="offers")
    name = models.CharField(max_length=125)
    price = models.FloatField()



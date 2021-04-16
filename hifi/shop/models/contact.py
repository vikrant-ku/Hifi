import datetime
from django.db import models
from django.utils import timezone



class Contact_Us(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subscribers(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
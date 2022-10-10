from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


class Movie(models.Model):
    name = models.CharField(max_legnth=100)
    genre = models.CharField(max_legth=80)
    relase_date = models.DateField()
    notice = models.CharField(default="this is just for ilustration purpose only")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length = 100, default="Addis Ababa")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

# Create your models here.

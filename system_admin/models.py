from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=55, unique=True)
    region = models.CharField(max_length=55, null=True)
    country = models.CharField(max_length=55, null=True, default='Ethiopia')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class Cinema(models.Model):
    name = models.CharField(max_length=50)
    admin = models.ManyToManyField(User, blank=True)
#   screen is used in place of hall the movie contains or as room of hotel
    number_of_screen = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    relative_location = models.TextField()
    absolute_location = models.TextField()
    picture = models.ImageField()
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Cast(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200,null =True)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name



 
class Crew(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=80)
    relase_date = models.DateField()
    poster = models.ImageField()
    cover = models.ImageField()
    cast = models.ManyToManyField(Cast, blank=True)
    crew = models.ManyToManyField(Crew, blank =True)
    trailer_link = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
from django.db import models
from cinema.models import MovieShow,MovieshowSeat
from django.contrib.auth.models import User

class Book(models.Model):
    movie_show_seat=models.ManyToManyField(MovieshowSeat,null=True,blank=True) 
    user = models.ForeignKey(User,on_delete=models.SET_NULL)
    price = models.FloatField()
    status = models.CharField(default="waiting",max_length=20,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.movie_show_seat
 

class Audience(models.Model): 
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True,blank=True)
    movie_show_seat = models.ForeignKey(MovieshowSeat,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=255, null=True)
    contact=models.CharField(max_length=255, null=True)

from email.policy import default
from django.db import models
from cinema.models import MovieShow,MovieshowSeat
from django.contrib.auth.models import User


# Create your models here.
class BookingRequest(models.Model):
    movie_show_seat = models.ForeignKey(MovieshowSeat,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.SET_NULL)
    price = models.FloatField()
    status = models.CharField(default="waiting",max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.movie_show_seat
 

from django.db import models
from cinema.models import MovieShow,MovieshowSeat
from user.models import Profile

class BookingRequest(models.Model):
    movie_show_seat=models.ManyToManyField(MovieshowSeat,blank=True) 
    user = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    price = models.FloatField()
    status = models.CharField(default="waiting",max_length=20,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
      ordering = ['status']

    def __str__(self):
        return self.movie_show_seat
 

class Audience(models.Model): 
    booking_request = models.ForeignKey(BookingRequest,on_delete=models.CASCADE,null=True,blank=True)
    movie_show_seat = models.ForeignKey(MovieshowSeat,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=255, null=True)
    contact=models.CharField(max_length=255, null=True)

    class Meta:
      ordering = ['booking_request']

    def __str__(self):
        return str(self.name)

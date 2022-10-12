from email.policy import default
from django.db import models
from system_admin.models import Cinema, Movie

class Screen(models.Model):
    cinema = models.ForeignKey(Cinema,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    feature = models.CharField(max_length = 100,null=True)
    number_of_seat = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Seat(models.Model):
    screen = models.ForeignKey(Screen,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=200,default="Normal")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

def __str__(self):
        return self.screen


class MovieShow(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.SET_NULL, null=True)
    screen = models.ForeignKey(Screen,on_delete=models.SET_NULL, null=True)
    schedule = models.DateTimeField()
    sold_ticket = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.price
# at the time cinemas screen have more than 1 seat type this will be useless
"""
the cinema admin will provide a  price of a type of seat that he have, than that will be placed in movieshow seat


"""
    
class MovieshowSeat(models.Model):
    movie_show = models.ForeignKey(MovieShow,on_delete=models.CASCADE) 
    seat = models.ForeignKey(Seat,on_delete=models.CASCADE)
    seat_type = models.CharField(max_length=50)
    price = models.FloatField() 
    reserved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.reserved
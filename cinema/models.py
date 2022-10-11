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


class MovieShow(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.SET_NULL, null=True)
    screen = models.ForeignKey(Screen,on_delete=models.SET_NULL, null=True)
    schedule = models.DateTimeField()
    price = models.FloatField()
    sold_ticket = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.price
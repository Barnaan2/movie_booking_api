from django.db import models
from cinema.models import MovieShow


# Create your models here.
class BookingRequest(models.Model):
    movie_show = models.ForeignKey(MovieShow,on_delete=models.CASCADE)
    user_email = models.CharField(max_length=200,null=True)
    user_phone_number = models.CharField(max_length=200)
    seat =models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.movie_show


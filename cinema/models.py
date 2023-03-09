from django.db import models
from movie.models import Movie
from user.models import Profile
from django.db.models.signals import post_save,post_delete



class City(models.Model):
    name = models.CharField(max_length=55, unique=True)
    region = models.CharField(max_length=55, null=True)
    picture = models.ImageField(blank=True,null=True)
    country = models.CharField(max_length=55, null=True, default='Ethiopia')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def city_name(self):
        return self.name
    def __str__(self):
        return str(self.name)


class Facility(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.name)
    

class Cinema(models.Model):
    name = models.CharField(max_length=50)
    admin = models.ManyToManyField(Profile, blank=True)
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
        return str(self.name)




class Screen(models.Model):
    cinema = models.ForeignKey(Cinema,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    facility = models.ManyToManyField(Facility,blank=True)
    number_of_seat = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.name)


class MovieShow(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.SET_NULL, null=True,blank=True)
    screen = models.ForeignKey(Screen,on_delete=models.SET_NULL, null=True)
    schedule = models.DateTimeField()
    price = models.FloatField() 
    sold_ticket = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['schedule']

    def __str__(self):
        return self.movie

    
class MovieshowSeat(models.Model):
    movie_show = models.ForeignKey(MovieShow,on_delete=models.SET_NULL,null=True,blank=True) 
    seat_number = models.IntegerField()
    reserved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __int__(self):
        return int(self.seat_number)
    

#------------------------------------------

# SIGNALS TO BE MOVED TO THE SIGNAL.PY FILE LATER

#-------------------------------------------
def create_movieshow_seat(sender,instance,created,**kwargs):
    if(created):
        movie_show = instance
        #python range never includes the last index so we add one to the original number
        seats = int(movie_show.screen.number_of_seat) + 1
        for seat in range(1,seats):
            MovieshowSeat.objects.create(movie_show=movie_show,seat_number=seat)


post_save.connect(create_movieshow_seat,sender=MovieShow)
            

def update_screen_seat(sender,instance,created, **kwargs):
    screen = instance
    if not created:
        screen_seats = MovieshowSeat.objects.filter(movie_show__screen=screen)
        for screen_seat in screen_seats:
            if not screen_seat.reserved:
                if screen_seat.seat_number > screen.number_of_seat:
                    screen_seat.delete()
post_save.connect(update_screen_seat,sender=Screen)



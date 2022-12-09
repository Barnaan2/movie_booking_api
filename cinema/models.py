from django.db import models
from system_admin.models import Cinema, Movie
from django.db.models.signals import post_save,post_delete

class Facility(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

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


        """
        if number_of_seat = m:
                seat = m
                seat.save()
       

        """

# class Seat(models.Model):
#     screen = models.ForeignKey(Screen,on_delete=models.CASCADE,null=True)
#     type = models.CharField(max_length=200,default="Normal")
#     seat = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
# def __str__(self):
#         return self.screen

"""




"""
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

# at the time cinemas screen have more than 1 seat type this will be useless
"""
the cinema admin will provide a  price of a type of seat that he have, than that will be placed in movieshow seat
 
 based on the price provided by the cinema admin  i will do where seat.type == something the price

 50

 :
 add price for each seat type
 input seat.type  price == request.price
 OKAY THE SUDO CODE IS AS FOLLOW


   seat_types = seat.object.filter(screen = screen)
for(type = in seat_types ):
    i = 0
    j =  type.seat

    while(i<j):
        MovieshowSeat.create(movie_show=movie_show,seat=seat_type,type= type.type,price = request.get(name=type.type))   
        i++
"""
    
class MovieshowSeat(models.Model):
    movie_show = models.ForeignKey(MovieShow,on_delete=models.SET_NULL,null=True,blank=True) 
    seat_number = models.IntegerField()
    reserved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __int__(self):
        return int(self.seat_number)
    

# signals
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



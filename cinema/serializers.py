
from rest_framework import serializers
from user.serializers import ProfileSerializer
from movie.serializers import MovieSerializer
from . models import MovieshowSeat,MovieShow,Screen,Facility,Screen,Cinema,City


class CitySerializer(serializers.ModelSerializer):
   class Meta:
      model = City
      fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
   class Meta:
      model = Facility
      fields = '__all__'
  
      

class CinemaSerializer(serializers.ModelSerializer):
   city = CitySerializer(many=False)
   admin = ProfileSerializer(many=True)
   class Meta:
      model = Cinema
      fields = '__all__'
           

      
class ScreenSerializer(serializers.ModelSerializer):
   facility = FacilitySerializer(many=True)
   cinema = CinemaSerializer(many=False)
   class Meta:
      model = Screen
      fields = '__all__'



class MovieShowSerializer(serializers.ModelSerializer):
   movie = MovieSerializer(many=False)
   screen = ScreenSerializer(many=False)
   class Meta:
      model = MovieShow
      fields = '__all__'

      
class MovieShowSeatSerializer(serializers.ModelSerializer):
   movie_show = MovieShowSerializer(many=False)
   class Meta:
      model =MovieshowSeat
      fields = '__all__'
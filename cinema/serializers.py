
from rest_framework import serializers
from . models import MovieshowSeat,MovieShow,Screen


class ScreenSerializer(serializers.ModelSerializer):
   class Meta:
      model = Screen
      fields = '__all__'



class MovieShowSerializer(serializers.ModelSerializer):
   class Meta:
      model = MovieShow
      fields = '__all__'

      
class MovieShowSeatSerializer(serializers.ModelSerializer):
   class Meta:
      model =MovieshowSeat
      fields = '__all__'
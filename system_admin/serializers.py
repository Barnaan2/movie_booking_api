
from rest_framework import serializers
from . models import Cinema, Movie,Crew,City,Cast


class CastSerializer(serializers.ModelSerializer):
   class Meta:
      model = Cast
      fields = '__all__'
   
class CitySerializer(serializers.ModelSerializer):
   class Meta:
      model = City
      fields = '__all__'
   
class CrewSerializer(serializers.ModelSerializer):
   class Meta:
      model = Crew
      fields = '__all__'
   
class MovieSerializer(serializers.ModelSerializer):
   class Meta:
      model = Movie
      fields = '__all__'

class CinemaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Cinema
      fields = '__all__'

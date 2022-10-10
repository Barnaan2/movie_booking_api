
from rest_framework import serializers
from . models import Cinema, Movie


class MovieSerializer(serializers.ModelSerializer):
   class Meta:
      model = Movie
      fields = '__all__'

class CinemaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Cinema
      fields = '__all__'
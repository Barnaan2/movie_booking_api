from dataclasses import field
from rest_framework import serializers
from . models import Cinema, Movie


class MovieSerializer(serializers.Serializer):
   class Meta:
      model = Movie
      field = '__all__'

class Cinema(serializers.Serializer):
   class Meta:
      model = Cinema
      field = '__all__'
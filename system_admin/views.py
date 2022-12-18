from django.shortcuts import render
from rest_framework.response import Response
from . models import Cinema,Movie,Crew,Cast,City
from . serializers import CinemaSerializer,MovieSerializer,CrewSerializer,CastSerializer,CitySerializer
# just to turn the reponse to the django restframe work view
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    endpoints = {
        'Movies':'http://127.0.0.1:8000/movies/',
        'cinema': 'http://127.0.0.1:8000/cinema/',
        'Cast':'http://127.0.0.1:8000/cast/',
        'crew': 'http://127.0.0.1:8000/crew/',
         'city': 'http://127.0.0.1:8000/city/'
    }
    return Response(endpoints)

@api_view(['GET'])
def movies(request):
    movies = Movie.objects.all()
    serialized_movie = MovieSerializer(movies,many=True)
    return Response(serialized_movie.data)


@api_view(['GET'])
def cinema(request):
    cinemas = Cinema.objects.all()
    serialzed_cinema = CinemaSerializer(cinemas,many=True)
    return Response(serialzed_cinema.data)

@api_view(['GET'])
def crew(request):
    crew = Crew.objects.all()
    serialzed_crew = CrewSerializer(crew,many=True)
    return Response(serialzed_crew.data)

@api_view(['GET'])
def cast(request):
    cast = Cast.objects.all()
    serialzed_cast = CastSerializer(cast,many=True)
    return Response(serialzed_cast.data)

@api_view(['GET'])
def city(request):
    city = City.objects.all()
    serialzed_city = CitySerializer(city,many=True)
    return Response(serialzed_city.data)
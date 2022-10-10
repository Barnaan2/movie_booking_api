from django.shortcuts import render
from rest_framework.response import Response
from . models import Cinema,Movie
from . serializers import CinemaSerializer,MovieSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    endpoints = {
        'Movies':'http://127.0.0.1:8000/movies/',
        'cinema': 'http://127.0.0.1:8000/cinema/'
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
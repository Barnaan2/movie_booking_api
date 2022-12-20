from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from . models import Movie,Crew,Cast
from cinema.models import Cinema
from cinema.serializers import CinemaSerializer
from . serializers import MovieSerializer,CrewSerializer,CastSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import serializers

@api_view(['GET']) 
def index(request):
    endpoints = {
        'Movies':'http://127.0.0.1:8000/movies/',
        'cinema': 'http://127.0.0.1:8000/cinema/',
        'Cast':'http://127.0.0.1:8000/cast/',
        'crew': 'http://127.0.0.1:8000/crew/'
        
    }
    return Response(endpoints)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
    return Response(serialzed_cast.data,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def add_cast(request):
    name = request.POST['name']
    role = request.POST['role']
    if(role == 'barnaan'):
         raise serializers.ValidationError('Validation that will be done in validation.py')
    about = request.POST['about']
    Cast.objects.create(name=name,role=role,about=about)
    
    return Response(status=status.HTTP_201_CREATED)


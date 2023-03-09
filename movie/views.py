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
from .validator import cast_validator
from django.core.files.storage import FileSystemStorage
import geoip2.database
import logging


# THE __name__ is used to log the file in the current module format or by the name of the current module
logger = logging.getLogger(__name__)
@api_view(['GET']) 
def index(request):
    user_os = request.META.get('HTTP_USER_AGENT','')
    user_ip = request.META.get('REMOTE_ADDR')
    logger.info(f'UserIP   {user_ip} , Acessing , movie.index Device {user_os}')
    geoip_reader =  geoip2.database.Reader('/home/barnaan/Desktop/GeoLite2-Country.mmdb')
    try:
        response = geoip_reader.country(user_ip)
        country = response.country.iso_code
    except geoip2.errors.AddressNotFoundError:
        country = 'Unknown'

    geoip_reader.close()

    endpoints = {
        'YOUR IP ADDRESS':f'we track your ip address {user_ip}',
        'YOur COuntry':f'your are from {country}',
        'Movies':'http://192.168.0.24:8000/movies/',
        'cinema': 'http://192.168.0.24:8000/cinema/',
        'Cast':'http://192.168.0.24:8000/cast/',
        'crew': 'http://192.168.0.24:8000/crew/'
        
    }
    return Response(endpoints)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movies(request):
    movies = Movie.objects.all()
    serialized_movie = MovieSerializer(movies,many=True)
    return Response(serialized_movie.data,status.HTTP_200_OK)


@api_view(['GET'])
def cinema(request):
    cinemas = Cinema.objects.all()
    serialzed_cinema = CinemaSerializer(cinemas,many=True)
    return Response(serialzed_cinema.data,status.HTTP_200_OK)

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


# @api_view(['POST'])
# def add_cast(request):
#     print(request.data)
#     serializer = CastSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#     else:
#         return Response(status = status.HTTP_400_BAD_REQUEST)
    

# @api_view(['POST'])
# def add_cast(request):
#     serializer = CastSerializer(data = request.data)
#     if serializer.is_valid():
#         if request.FILES.get('image'):
#            image = request.FILES['image']
#            store_image = FileSystemStorage()
#            name = store_image.save('images/' + image.name, image)
#            serializer.validated_data['image'] = name
#            print(serializer)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from django.contrib.staticfiles.storage import staticfiles_storage

@api_view(['POST'])
def add_cast(request):
    serializer = CastSerializer(data=request.data)
    if serializer.is_valid():
        if request.FILES.get('image'):
            image = request.FILES['image']
            store_image = FileSystemStorage()
            name = store_image.save(image.name, image)
            serializer.validated_data['image'] = staticfiles_storage.url(name)  # Get the URL of the stored image
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from movie.models import Movie,Crew,Cast
from cinema.models import Cinema,City,Facility
from payment.models import PaymentMethod
# from cinema.serializers CinemaSerializer
# from . serializers import MovieSerializer,CrewSerializer,CastSerializer,CitySerializer
# # just to turn the reponse to the django restframe work view
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser


@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_movie(request):
    cinemas = Movie.objects.create()
    
    return HttpResponse('You have added new Item')


@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_cinema(request):
    cinemas = Cinema.objects.create()
    
    return HttpResponse('You have added new Item')



@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_city(request):
     
    City.objects.create()
    return HttpResponse('You have added new city')



@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_cast(request):
     
    Cast.objects.create()
    return HttpResponse('You have added new cast')



@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_crew(request):
     
    Crew.objects.create()
    return HttpResponse('You have added new crew')


@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_facility(request):
     
    Facility.objects.create()
    return HttpResponse('You have added new crew')

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_payment_method(request):
    
    PaymentMethod.objects.create()
    return HttpResponse('You have added new crew')
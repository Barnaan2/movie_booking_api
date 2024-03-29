from django.shortcuts import render,HttpResponse
from . models import City,Cinema,Facility,Screen,MovieShow,MovieshowSeat
from . serializers import CitySerializer,CinemaSerializer,FacilitySerializer,ScreenSerializer,MovieShowSerializer,MovieshowSeat
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def city(request):
    city = City.objects.all()
    serialzed_city = CitySerializer(city,many=True)
    return Response(serialzed_city.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cinema(request):
    cinema = Cinema.objects.all()
    cinema_data = CinemaSerializer(cinema,many=True)
    return Response(cinema_data.data)

@api_view(['GET'])
def facility(request):
    facility = Facility.objects.all()
    facility_data = FacilitySerializer(facility,many=True)
    return Response(facility_data.data)
 
@api_view(['POST'])
def add_facility(request):
    facl = FacilitySerializer(data=request.data)
    if facl.is_valid():
        facl.save()
        return Response(facl.data,status=status.HTTP_201_CREATED)
    else: 
        return Response(status=status.HTTP_400_BAD_REQUEST)
 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_crew(request):
    serl_crew = CrewSerializer(data=request.data)
    if serl_crew.is_valid():
        serl_crew.save()
        return Response(serl_crew.data,status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_screen(request):
     
    Screen.objects.create()
    return HttpResponse('You have added new crew')
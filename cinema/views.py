from django.shortcuts import render
from . models import City,Cinema,Facility,Screen,MovieShow,MovieshowSeat
from . serializers import CitySerializer,CinemaSerializer,FacilitySerializer,ScreenSerializer,MovieShowSerializer,MovieshowSeat
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
def city(request):
    city = City.objects.all()
    serialzed_city = CitySerializer(city,many=True)
    return Response(serialzed_city.data)


@api_view(['GET'])
@permission_classes(IsAuthenticated)
def cinema(request):
    cinema = Cinema.objects.all()
    cinema_data = CinemaSerializer(cinema,many=True)
    return Response(cinema_data.data)

@api_view(['GET'])
def facility(request):
    facility = Facility.objects.all()
    facility_data = FacilitySerializer(facility,many=True)
    return Response(facility_data.data)
 

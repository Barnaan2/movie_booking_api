from django.shortcuts import render
from . models import City
from . serializers import CitySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def city(request):
    city = City.objects.all()
    serialzed_city = CitySerializer(city,many=True)
    return Response(serialzed_city.data)
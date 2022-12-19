from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BookingRequest
from .serializers import BookingRequestSerializer


@api_view(['GET'])
def booking(request):
    booking_request = BookingRequest.objects.all()
    booking_request_data = BookingRequestSerializer(booking_request,many=True)
    return Response(booking_request_data.data)
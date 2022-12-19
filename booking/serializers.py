
from rest_framework import serializers
from . models import BookingRequest,Audience


class BookingRequestSerializer(serializers.ModelSerializer):
   class Meta:
      model = BookingRequest
      fields = '__all__'


class AudienceSerializer(serializers.ModelSerializer):
   #movieshow seat
   booking_request = BookingRequestSerializer(many=False)
   class Meta:
       model = Audience
       fields = '__all__'
       
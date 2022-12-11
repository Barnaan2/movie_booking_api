
from rest_framework import serializers
from . models import BookingRequest


class BookSerializer(serializers.ModelSerializer):
   class Meta:
      model = BookingRequest
      fields = '__all__'



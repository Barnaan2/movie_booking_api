
from rest_framework import serializers
from . models import BookingRequest,Audience
from user.serializers import ProfileSerializer
from  cinema.serializers import CinemaSerializer,MovieShowSeatSerializer


class BookingRequestSerializer(serializers.ModelSerializer):
   cinema = CinemaSerializer(many=False)
   user = ProfileSerializer(many=True)
   movie_show_seat = MovieShowSeatSerializer(many=True)
   class Meta:
      model = BookingRequest
      fields = '__all__'


class AudienceSerializer(serializers.ModelSerializer):
   movie_show_seat = MovieShowSeatSerializer(many=False)
   booking_request = BookingRequestSerializer(many=False)
   class Meta:
       model = Audience
       fields = '__all__'
       
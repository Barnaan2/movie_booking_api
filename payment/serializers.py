
from rest_framework import serializers
from . models import PaymentInformation,PaymentMethod,Paid
from cinema.serializers import CinemaSerializer
from user.serializers import ProfileSerializer
from booking.serializers import BookingRequestSerializer



class PaymentInformationSerializer(serializers.ModelSerializer):
   cinema = CinemaSerializer(many=False)
   added_by = ProfileSerializer(many=False)
   class Meta:
      model = PaymentInformation
      fields = '__all__'




class PaymentMethodSerializer(serializers.ModelSerializer):
   class Meta:
      model = PaymentMethod
      fields = '__all__'

 
class PaidSerializer(serializers.ModelSerializer):
   payment_info = PaymentInformationSerializer(many=False)
   booking_request = BookingRequestSerializer(many=False)
   class Meta:
      model = Paid
      fields = '__all__'
      
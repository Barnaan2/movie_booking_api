
from rest_framework import serializers
from . models import PaymentInformation,PaymentMethod


class PaymentInformationSerializer(serializers.ModelSerializer):
   class Meta:
      model = PaymentInformation
      fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
   class Meta:
      model = PaymentMethod
      fields = '__all__'

# class FinishPaymentSerializer(serializers.ModelSerializer):
#    class Meta:
#       model = FinishPayment
#       fields = '__all__'
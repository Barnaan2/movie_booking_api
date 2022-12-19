from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import PaymentMethod,PaymentInformation,Paid
from . serializers import PaymentMethodSerializer,PaymentInformationSerializer,PaidSerializer


@api_view(['GET'])
def payment_method(request):
    payment_method = PaymentMethod.objects.all()
    payment_method_data = PaymentMethodSerializer(payment_method,many=True)
    return Response(payment_method_data.data)


@api_view(['GET'])
def payment_information(request):
    payment_information = PaymentInformation.objects.all()
    payment_information_data = PaymentInformationSerializer(payment_information,many=True)
    return Response(payment_information_data.data)


@api_view(['GET'])
def paid(request):
    paid = Paid.objects.all()
    paid_data = PaidSerializer(paid,many=True)
    return Response(paid_data.data)


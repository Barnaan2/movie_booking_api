from rest_framework import serializers


def cast_validator(data):
 if(data == 'barnaan'):
         raise serializers.ValidationError('Validation that will be done in validation.py')
 else:
     return data
     


from rest_framework import serializers
from .models import Profile,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Profile
        fields = '__all__'
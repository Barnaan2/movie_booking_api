from rest_framework import serializers
from . models import  Movie,Crew,Cast


class CastSerializer(serializers.ModelSerializer):
   class Meta:
      model = Cast
      fields = '__all__'
   

   
class CrewSerializer(serializers.ModelSerializer):
   class Meta:
      model = Crew
      fields = '__all__'
   
class MovieSerializer(serializers.ModelSerializer):
   cast = CastSerializer(many=True)
   crew = CrewSerializer(many=True)
   # crew_data = serializers.SerializerMethodField()
   class Meta:
      model = Movie
      fields = '__all__'
   # def get_crew_data(self,obj):
   #     crew = obj.objects.all()
   #     datax = CrewSerializer(crew, many=True)
   #     return datax.data


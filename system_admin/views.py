from django.shortcuts import render
from rest_framework.response import Response
from . models import Cinema,Movie
from . serializers import CinemaSerializer,MovieSerializer

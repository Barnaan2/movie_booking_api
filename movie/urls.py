
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('movies/',views.movies),
    path('cinema/',views.cinema),
    path('crew/',views.crew),
    path('cast/',views.cast),
]
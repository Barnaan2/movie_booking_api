
from django.urls import path
from . import views

urlpatterns = [
     path('cities/',views.city),
     path('facilities/',views.facility),
    path('cinemas/',views.cinema),
]


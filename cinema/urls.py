
from django.urls import path
from . import views

urlpatterns = [
     path('cities/',views.city,name="city"),
     path('facilities/',views.facility),
     path('add-facl/',views.add_facility,name="add-facility"),
    path('cinemas/',views.cinema),
    path('add-screen',views.add_screen)
]


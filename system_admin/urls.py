
from django.urls import path
from . import views

urlpatterns = [
    path('add-movie/',views.add_movie),
    path('add-cinema/',views.add_cinema),
    path('add-city/',views.add_city),
    path('add-crew/',views.add_crew),
    path('add-cast/',views.add_cast),
      path('add-payment-method/',views.add_payment_method),
]

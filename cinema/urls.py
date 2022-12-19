
from django.urls import path
from . import views

urlpatterns = [
     path('city/',views.city),
    # path('movies/',views.movies),
    # path('cinema/',views.cinema),
]


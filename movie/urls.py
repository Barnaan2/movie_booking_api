
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('movies/',views.movies),
    path('cinema/',views.cinema),
    path('crew/',views.crew),
    path('cast/',views.cast),
    path('add-cast/',views.add_cast)
]
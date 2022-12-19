from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('profile/',views.profile_data),
    path('update-profile/',views.update_profile,name="update-profile"),
    path('register/',views.register,name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
]
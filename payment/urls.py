
from django.urls import path
from . import views

urlpatterns = [
    path('payment-method',views.payment_method),
    path('payment-information/',views.payment_information),
    path('paid/',views.paid),
]

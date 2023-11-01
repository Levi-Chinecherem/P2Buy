# payments/urls.py

from django.urls import path
from .views import initiate_payment

urlpatterns = [
    path('initiate_payment/<int:order_id>/', initiate_payment, name='initiate_payment'),
    # Add other payment-related URLs as needed
]

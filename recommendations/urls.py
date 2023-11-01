# recommendations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('recommendations/<int:product_id>/', views.product_recommendations, name='product_recommendations'),
]

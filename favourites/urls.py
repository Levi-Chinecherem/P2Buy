from django.urls import path
from . import views

urlpatterns = [
    path('add_to_favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('favorite_list/', views.favorite_list, name='favorite_list'),
    path('filter_favorites/', views.filter_favorites, name='filter_favorites'),
]

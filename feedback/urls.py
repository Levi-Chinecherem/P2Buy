from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.feedback_list, name='feedback_list'),
    path('create/', views.feedback_create, name='feedback_create'),
    path('<int:feedback_id>/update/', views.feedback_update, name='feedback_update'),
    path('<int:feedback_id>/delete/', views.feedback_delete, name='feedback_delete'),
]

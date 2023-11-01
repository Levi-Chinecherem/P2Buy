from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='notification_list'),
    path('mark_as_read/<int:notification_id>/', views.mark_notification_as_read, name='mark_as_read'),
]

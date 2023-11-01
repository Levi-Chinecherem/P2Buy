# urls.py in the "groups" app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroupListView.as_view(), name='group_list'),
    path('<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('create/', views.GroupCreateView.as_view(), name='group_create'),
    path('<int:pk>/update/', views.GroupUpdateView.as_view(), name='group_update'),
    path('<int:pk>/delete/', views.GroupDeleteView.as_view(), name='group_delete'),
    path('<int:group_id>/checkout/', views.checkout, name='checkout'), 
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/failure/', views.payment_failure, name='payment_failure'),
]
# urls.py in the "groups" app
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    # Define the 'add_to_group' URL pattern
    path('<int:product_id>/add_to_group/<int:group_id>/', views.add_to_group, name='add_to_group'),
    path('', views.GroupListView.as_view(), name='group_list'),
    path('<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('create//<int:product_id>/', views.GroupCreateView.as_view(), name='group_create'),
    path('<int:pk>/update/', views.GroupUpdateView.as_view(), name='group_update'),
    path('<int:pk>/delete/', views.GroupDeleteView.as_view(), name='group_delete'),
    path('<int:group_id>/checkout/', views.checkout, name='checkout'), 
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/failure/', views.payment_failure, name='payment_failure'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
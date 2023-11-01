from django.urls import path
from .views import UserProfileCreateUpdateView, CustomLoginView, CustomPasswordChangeView, CustomPasswordResetView, CustomPasswordResetConfirmView, CustomLogoutView, CustomRegisterView

urlpatterns = [
    path('profile/', UserProfileCreateUpdateView.as_view(), name='userprofile'),
    
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('register/', CustomRegisterView.as_view(), name='register'),
]

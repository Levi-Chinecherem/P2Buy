from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm  # Custom registration form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import UserProfile

class UserProfileCreateUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'accounts/userprofile_form.html'
    success_url = reverse_lazy('userprofile')  # Redirect to the user's profile page

    def get_object(self, queryset=None):
        # Get the user's profile if it exists, otherwise create a new one
        return self.request.user.userprofile

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Custom login template

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'  # Custom password change template
    success_url = reverse_lazy('password_change_done')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'  # Custom password reset template
    email_template_name = 'registration/password_reset_email.html'  # Custom email template
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'  # Custom password reset confirm template

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirect to the login page after logout

class CustomRegisterView(CreateView):
    template_name = 'registration/register.html'  # Custom registration template
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirect to the login page after registration

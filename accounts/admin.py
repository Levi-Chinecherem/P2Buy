from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'

class UserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)

# Unregister the built-in User model
admin.site.unregister(User)

# Register the User model with the custom admin class
admin.site.register(User, UserAdmin)

# Set the site header, title, and URL
admin.site.site_header = "P2Buy Administration"
admin.site.site_title = "P2Buy Admin"
admin.site.site_url = "/home"

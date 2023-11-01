# recommendations/admin.py
from django.contrib import admin
from .models import UserInteraction

class UserInteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'interaction_type')
    list_filter = ('interaction_type',)
    search_fields = ('user__username', 'product__name')
    list_per_page = 20

# Register the UserInteraction model with the custom admin class
admin.site.register(UserInteraction, UserInteractionAdmin)

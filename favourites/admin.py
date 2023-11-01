# favorites/admin.py
from django.contrib import admin
from .models import Favorite

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_per_page = 10

# Register the Favorite model with the custom admin class
admin.site.register(Favorite, FavoriteAdmin)

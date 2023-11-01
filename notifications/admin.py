# notifications/admin.py
from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('user__username', 'subject')
    list_per_page = 20

# Register the Notification model with the custom admin class
admin.site.register(Notification, NotificationAdmin)

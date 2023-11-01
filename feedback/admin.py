# feedback/admin.py
from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username', 'title')
    list_per_page = 10

# Register the Feedback model with the custom admin class
admin.site.register(Feedback, FeedbackAdmin)

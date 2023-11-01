# groups/admin.py
from django.contrib import admin
from .models import Group, Order

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'quantity', 'total_amount')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'status')
    list_per_page = 10

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'total_amount', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'product__name', 'payment_method')
    list_per_page = 10

# Register the Group and Order models with the custom admin classes
admin.site.register(Group, GroupAdmin)
admin.site.register(Order, OrderAdmin)

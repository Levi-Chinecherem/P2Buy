# products/admin.py
from django.contrib import admin
from .models import Product, ProductCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    list_per_page = 20

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 20

# Register the Product and ProductCategory models with the custom admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)

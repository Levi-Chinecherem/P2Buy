# dashboard/views.py
from django.shortcuts import render
from products.models import Product
from favorites.models import Favorite
from groups.models import Group

def dashboard(request):
    # Fetch data for your charts
    product_count = Product.objects.count()
    favorite_count = Favorite.objects.count()
    group_count = Group.objects.count()
    
    return render(request, 'dashboard.html', {
        'product_count': product_count,
        'favorite_count': favorite_count,
        'group_count': group_count,
    })

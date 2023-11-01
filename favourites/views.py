# favorites/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Favorite
from products.models import Product
from .forms import FavoritesFilterForm
from django.db.models import Q

@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, 'Added to Favorites')
    else:
        messages.info(request, 'This product is already in your Favorites')

    return redirect('product_detail', product_id=product_id)

@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite = Favorite.objects.filter(user=request.user, product=product)

    if favorite.exists():
        favorite.delete()
        messages.success(request, 'Removed from Favorites')
    else:
        messages.info(request, 'This product is not in your Favorites')

    return redirect('product_detail', product_id=product_id)


@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    
    return render(request, 'favorites/favorite_list.html', {'favorites': favorites})

@login_required
def filter_favorites(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    
    filtered_favorites = Favorite.objects.filter(user=request.user)
    
    if query:
        filtered_favorites = filtered_favorites.filter(Q(product__name__icontains=query) | 
                                                      Q(product__short_description__icontains=query))
    
    if category:
        filtered_favorites = filtered_favorites.filter(product__category__name=category)
    
    return render(request, 'favorites/favorite_list.html', {'filtered_favorites': filtered_favorites})

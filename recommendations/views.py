# recommendations/views.py
from django.shortcuts import render
from .recommendations import ContentBasedRecommendation
from products.models import Product

def product_recommendations(request, product_id):
    # Fetch the product's description
    product = Product.objects.get(pk=product_id)
    
    # Fetch all products' descriptions
    products = Product.objects.all().values('id', 'description')
    
    # Initialize the recommendation system
    recommendation_system = ContentBasedRecommendation(products)
    
    # Get recommendations for the given product
    recommendations = recommendation_system.get_recommendations(product_id)
    
    return render(request, 'recommendations/recommendations.html', {'recommendations': recommendations})

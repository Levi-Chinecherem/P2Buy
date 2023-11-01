from django import forms
from .models import Favorite
from django.db.models import Q

class FavoritesFilterForm(forms.Form):
    search = forms.CharField(label='Search', required=False)
    min_price = forms.DecimalField(label='Min Price', required=False)
    max_price = forms.DecimalField(label='Max Price', required=False)
    category = forms.CharField(label='Category', required=False)

    def filter_favorites(self, favorites):
        search_query = self.cleaned_data.get('search')
        min_price = self.cleaned_data.get('min_price')
        max_price = self.cleaned_data.get('max_price')
        category = self.cleaned_data.get('category')

        # Start with an empty Q object
        q = Q()

        if search_query:
            # Add search filter if search query is provided
            q &= (Q(product__name__icontains=search_query) |
                  Q(product__short_description__icontains=search_query))

        if min_price:
            # Add min_price filter if provided
            q &= Q(product__amount__gte=min_price)

        if max_price:
            # Add max_price filter if provided
            q &= Q(product__amount__lte=max_price)

        if category:
            # Add category filter if provided
            q &= Q(product__category__name__icontains=category)

        # Apply the filter to the favorites queryset
        return favorites.filter(q)

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Product, ProductCategory
from .forms import ProductForm
from django.urls import reverse_lazy
from groups.models import Group

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Create a dictionary to store product-group associations
        product_groups = {}
        
        for product in context['products']:
            # Retrieve the group for the current product, if it exists
            group = Group.objects.filter(product=product).first()
            
            if group:
                # Store the group ID in the dictionary
                product_groups[product.id] = group.id
            else:
                # If no group exists, you can set it to None or any default value
                product_groups[product.id] = None
        
        context['product_groups'] = product_groups  # Add the dictionary to the context
        
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Limit the similar products to 6
        context['similar_products'] = self.object.get_similar_products()[:6]
        # Get the group for the current product
        context['group'] = Group.objects.filter(product=self.object).first()
        return context

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = '/products/'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user when creating a product
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = '/products/'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'  # Create this template
    success_url = reverse_lazy('product_list')

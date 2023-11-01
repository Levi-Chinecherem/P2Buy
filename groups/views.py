# views.py in the "groups" app
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Group
from .forms import GroupForm, CheckoutForm
from django.urls import reverse_lazy
from django.utils import timezone
from products.models import Product
from django.contrib.auth.decorators import login_required
from payments.views import initiate_payment
from django.urls import reverse

@login_required
def add_to_group(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Check if a group for this product already exists
    try:
        group = Group.objects.get(product=product)
    except Group.DoesNotExist:
        # If the group doesn't exist, create a new group
        group = Group.objects.create(product=product)
    
    # Add the product to the group
    group.products.add(product)
    
    # Redirect to the appropriate view, e.g., the product detail view
    return redirect('product_detail', product_id=product_id)

class GroupListView(ListView):
    model = Group
    template_name = 'groups/group_list.html'
    context_object_name = 'groups'

class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/group_detail.html'
    context_object_name = 'group'

class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/group_form.html'
    success_url = reverse_lazy('group_list')

    def form_valid(self, form):
        product_id = self.kwargs['product_id']  # Get the product ID from the URL
        product = get_object_or_404(Product, id=product_id)
        form.instance.product = product  # Set the product instance for the group
        form.instance.name = product.name  # Automatically set name
        form.instance.short_description = product.short_description  # Automatically set short_description
        form.instance.group_image = product.product_cover_image.url  # Automatically set group_image
        form.instance.status = "Pending"
        form.instance.quantity = 1
        form.instance.total_amount = product.amount * form.instance.quantity
        return super().form_valid(form)

class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/group_form.html'
    success_url = '/groups/'

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/group_confirm_delete.html'  # Create this template
    success_url = '/groups/'


@login_required
def checkout(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.group = group
            order.quantity = group.quantity
            order.amount = group.total_amount  # Use the calculated total amount
            order.save()

            # Now, initiate the payment for this order
            response = initiate_payment(request, order)

            if response.status_code == 200:
                return redirect('payment_success')
            else:
                return redirect('payment_failure')
    else:
        form = CheckoutForm()

    return render(request, 'groups/checkout.html', {'form': form, 'group': group})

@login_required
def payment_success(request):
    return render(request, 'groups/payment_success.html')

@login_required
def payment_failure(request):
    return render(request, 'groups/payment_failure.html')
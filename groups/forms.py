# forms.py in the "groups" app
from django import forms
from .models import Group, Order
from django.utils import timezone

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_region']
        
    def set_group_details(self, product):
        # Set group details based on the product
        self.instance.name = f"{product.name}_{timezone.now()}"
        self.instance.group_image = product.product_cover_image
        self.instance.short_description = product.short_description
        self.instance.group_region = self.cleaned_data.get('group_region')

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'shipping_address', 'payment_method', 'additional_notes']

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'class': 'form-control', 'type': 'number', 'min': 1})
        self.fields['shipping_address'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_method'].widget.attrs.update({'class': 'form-control'})
        self.fields['additional_notes'].widget.attrs.update({'class': 'form-control', 'rows': 3})

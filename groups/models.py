from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class STATUS_CHOICES(models.TextChoices):
    OPEN = 'open', 'Open'
    ORDER_PROCESSING = 'order_processing', 'Order Processing'
    CLOSED = 'closed', 'Closed'
    RECEIVED = 'received', 'Received'

class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    group_image = models.ImageField(upload_to='groups/', null=True, blank=True)
    short_description = models.TextField()
    group_region = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES.OPEN)
    
    # Add quantity and total amount fields
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product in the order
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Total cost of the order
    shipping_address = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=100)
    additional_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def save(self, *args, **kwargs):
        # Calculate the total amount based on the product's amount and quantity
        self.total_amount = self.product.amount * self.quantity
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f'Order for {self.product.name} by {self.user.username}'

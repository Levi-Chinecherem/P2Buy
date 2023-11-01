# recommendations/models.py
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=20)  # e.g., "view", "purchase", "like"

    def __str__(self):
        return f'{self.user.username} - {self.product.name} ({self.interaction_type})'

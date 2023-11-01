# models.py in the "products" app
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    product_cover_image = models.ImageField(upload_to='products/', null=True, blank=True)
    content = RichTextUploadingField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_similar_products(self):
        return Product.objects.filter(category=self.category).exclude(id=self.id)

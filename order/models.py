from django.db import models
from products.models import Product

class Order(models.Model):
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

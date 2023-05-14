from django.db import models
from products.models import Product
from authapi.models import User


class Feedback(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    user=models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    rating = models.IntegerField()
    

    def __str__(self):
        return self.user
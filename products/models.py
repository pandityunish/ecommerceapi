from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()


    def __str__(self):
        return self.product_name

class ProductsImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,                                                    related_name='images')
    image = models.ImageField(upload_to="products/images")


    def __str__(self):
        return "%s" % (self.product.product_name)
class Sliders(models.Model):
    image = models.ImageField(upload_to='products/images', default="")
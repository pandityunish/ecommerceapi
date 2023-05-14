from django.db import models

from category.models import Category

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    # subcategory = models.CharField(max_length=50, default='')

    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    def __str__(self):
        return self.product_name
        

class PopularProduct(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    # subcategory = models.CharField(max_length=50, default='')

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
    

class PopularProductsImage(models.Model):
    popularproduct=models.ForeignKey(PopularProduct,on_delete=models.CASCADE,)

    image = models.ImageField(upload_to="products/images")
 
    def __str__(self):
        return "%s" % (self.popularproduct.product_name)
    
class Sliders(models.Model):
    image = models.ImageField(upload_to='products/images', default="")

class Specialoffer(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=50)
    brand = models.IntegerField(default=0)
    image=models.ImageField(upload_to="products/images",default='')

    def __str__(self):
        return self.name
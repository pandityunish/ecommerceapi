from django.db import models

# Create your models here.
class Reviews(models.Model):
    review_id = models.AutoField
    username_name = models.CharField(max_length=50)
    userimage=models.CharField(max_length=1000)
    star = models.IntegerField(default=0)
    desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    product_id=models.CharField(max_length=160,default="0")
    def __str__(self):
        return self.username_name
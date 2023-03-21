from rest_framework import serializers
from products.models import Product


#create serializers here
class ProductSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model=Product
        fields="__all__"
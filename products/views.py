
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from products.serializers import ProductSerializer,SliderSerializers,SpecialOfferSerializers,PopularProductSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from products.models import Product,Sliders,Specialoffer,PopularProduct
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    parser_class = [MultiPartParser, FormParser]
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    
class PopularProductViewSet(viewsets.ModelViewSet):
    parser_class = [MultiPartParser, FormParser]
    queryset= PopularProduct.objects.all()
    serializer_class=PopularProductSerializer

class SliderViewSet(viewsets.ModelViewSet):
    queryset=Sliders.objects.all()
    serializer_class=SliderSerializers

class SpecialViewSet(viewsets.ModelViewSet):
    queryset=Specialoffer.objects.all()
    serializer_class=SpecialOfferSerializers

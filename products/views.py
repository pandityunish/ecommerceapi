
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from products.serializers import ProductSerializer,SliderSerializers
from rest_framework.parsers import MultiPartParser, FormParser
from products.models import Product,Sliders
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    parser_class = [MultiPartParser, FormParser]
    queryset= Product.objects.all()
    serializer_class=ProductSerializer

class SliderViewSet(viewsets.ModelViewSet):
    queryset=Sliders.objects.all()
    serializer_class=SliderSerializers

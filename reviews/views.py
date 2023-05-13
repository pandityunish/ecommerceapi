from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from reviews.models import Reviews
from reviews.serializers import ReviewSerializers
# Create your views here.
class ReviewViewSet(viewsets.ModelViewSet):
    parser_class = [MultiPartParser, FormParser]
    queryset= Reviews.objects.all()
    serializer_class=ReviewSerializers
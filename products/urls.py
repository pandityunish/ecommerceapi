from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from products.views import ProductViewSet,SliderViewSet
router= routers.DefaultRouter()
router.register(r'product', ProductViewSet),
router.register(r'sliders',SliderViewSet)
urlpatterns = [
    path('',include(router.urls))
]
from django.urls import path
from . import views



urlpatterns = [
    path('api/location/', views.LocationAPIView.as_view(), name='location-api'),
]

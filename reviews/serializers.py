from rest_framework import serializers
from reviews.models import Reviews

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Order
        fields = ('location', 'name', 'number', 'email', 'product', 'image')

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.location = validated_data.get('location', instance.location)
        instance.name = validated_data.get('name', instance.name)
        instance.number = validated_data.get('number', instance.number)
        instance.email = validated_data.get('email', instance.email)
        instance.product = validated_data.get('product', instance.product)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

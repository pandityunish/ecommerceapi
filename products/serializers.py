from rest_framework import serializers
from products.models import Product,ProductsImage,Sliders


#create serializers here
class ProductsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsImage
        fields = "__all__"
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    images =  ProductsImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    class Meta:
        model=Product
        fields="__all__"

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)

        for image in uploaded_images:
            ProductsImage.objects.create(product=product, image=image)

        return product
class SliderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        fields = "__all__"
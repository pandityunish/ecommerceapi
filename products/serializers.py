from rest_framework import serializers
from products.models import Product,ProductsImage,Sliders,Specialoffer,PopularProduct,PopularProductsImage


#create serializers here
# class ProductsImageSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ProductsImage
#         fields = "__all__"

class ProductsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsImage
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    images = ProductsImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        product = Product.objects.create(**validated_data)

        for image in uploaded_images:
            ProductsImage.objects.create(product=product, image=image)

        return product


class PopularProductsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularProductsImage
        fields = ('image',)


class PopularProductSerializer(serializers.ModelSerializer):
    images = PopularProductsImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    class Meta:
        model = PopularProduct
        fields = '__all__'

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = PopularProduct.objects.create(**validated_data)

        for image in uploaded_images:
            PopularProductsImage.objects.create(product=product, image=image)

        return product
    

class SliderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        fields = "__all__"

class SpecialOfferSerializers(serializers.ModelSerializer):
    class Meta:
        model = Specialoffer
        fields = "__all__"
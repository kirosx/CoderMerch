from rest_framework import serializers
from mainapp.models import ProductCategory, Product, ProductBySize, ProductImage


class ProductCategorySerializers(serializers.ModelSerializer):
    """СЕРРИАЛИЗАЦИЯ - КАТЕГОРИЯ ПРОДУКТА"""

    class Meta:
        model = ProductCategory
        fields = ('name_category', 'discount')


class ProductSerializers(serializers.ModelSerializer):
    """СЕРРИАЛИЗАЦИЯ - ПРОДУКТ"""
    category = ProductCategorySerializers()

    class Meta:
        model = Product
        fields = ('name_product', 'logotype', 'gender', 'color', 'article', 'price', 'discount', 'description', \
                  'category', 'get_size', 'get_img')


class ProductBySizeSerializers(serializers.ModelSerializer):
    """СЕРРИАЛИЗАЦИЯ - КОЛИЧЕСТВО ПРОДУКТОВ ПО РАЗМЕРАМ"""
    product = ProductSerializers()

    class Meta:
        model = ProductBySize
        fields = ('size', 'quantity', 'product')


class ProductImageSerializers(serializers.ModelSerializer):
    """СЕРРИАЛИЗАЦИЯ - ФОТОГРАФИИ ПРОДУКТА"""
    # product = ProductSerializers()

    class Meta:
        model = ProductImage
        fields = ('img_product', )
        # fields = ('img_product', 'product')

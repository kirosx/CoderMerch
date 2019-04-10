from django.shortcuts import render
from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import Http404
from django.contrib.auth.models import User

from mainapp.models import Product, ProductImage
from mainapp.serializers import ProductSerializers, ProductImageSerializers


class ProductsList(APIView):
    """ПОЛУЧЕНИЕ СПИСКА ВСЕХ ПРОДУКТОВ"""

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)


class ProductView(APIView):
    """ПОЛУЧЕНИЕ ДАННЫХ ПРОДУКТА ПО ПЕРВИЧНОМУ КЛЮЧУ"""

    def get(self, request, pk):
        try:
            products = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        # products = Product.objects.get(pk=pk)
        serializer = ProductSerializers(products)
        return Response(serializer.data)


class ProductCategory(APIView):
    """ПОЛУЧЕНИЕ ПРОДУКТОВ ПО КАТЕГОРИИ"""

    def get(self, request, category):
        products = Product.objects.filter(category__name_category=category)
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)


class ProductGender(APIView):
    """ПОЛУЧЕНИЕ ПРОДУКТОВ ПО ПОЛУ(мужское, женское, мальчики, девочки)"""
    # где gender пможет принимать следующие значения:
    #     'male' - Мужское;
    #     'female' - Женское;
    #     'boys' - Детское (мальчик);
    #     'girls' - Детское (девочка).

    def get(self, request, gender):
        products = Product.objects.filter(gender=gender)
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)


class ProductImg(APIView):
    """ПОЛУЧЕНИЕ ПРОДУКТОВ ПО ПОЛУ(мужское, женское, мальчики, девочки)"""

    def get(self, request):
        products = ProductImage.objects.all()
        serializer = ProductImageSerializers(products, many=True)
        return Response(serializer.data)



    # enderer_classes = [TemplateHTMLRenderer]
    # template_name = 'mainapp/product.html'
    #
    # def get(self, request, pk):
    #     product = Product.objects.filter(product_type__pk=pk)[0]
    #     print('*' * 50, request.method, '*' * 50)
    #     return Response({'product': product})
    #
    #


# renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'mainapp/product.html'
#
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductsSerializers(products, many=True)
#         return Response({'product': serializer})
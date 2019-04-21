from rest_framework import viewsets
from mainapp.serializers import ProductSerializer, ProductCategorySerializer
from mainapp.models import *
from rest_framework import permissions


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()



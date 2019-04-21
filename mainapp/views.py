from rest_framework import viewsets
from mainapp.serializers import *
from mainapp.models import *
from rest_framework import permissions
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductDetailSerializer(instance)
        return Response(serializer.data)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductSerializer(Product.objects.filter(category_id=instance.id), many=True)
        return Response(serializer.data)



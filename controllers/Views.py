from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import User
from mainapp.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


def home(request: HttpRequest):
    return render(request, 'index.html')


class ProductList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mainapp/test_page.html'

    def get(self, request):
        queryset = Product.objects.all()
        return Response({'product': queryset})


def about(request: HttpRequest):
    return render(request, 'about.html')


def products(request: HttpRequest):
    return render(request, 'products.html')


def product(request: HttpRequest):
    return render(request, 'product.html')

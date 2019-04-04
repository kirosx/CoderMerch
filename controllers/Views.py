from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):
    return render(request, 'index.html')


def about(request: HttpRequest):
    return render(request, 'about.html')


def products(request: HttpRequest):
    return render(request, 'products.html')

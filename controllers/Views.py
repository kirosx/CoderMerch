from django.shortcuts import render
from django.http import HttpRequest


def basket(request: HttpRequest):
    return render(request, 'basket.html')

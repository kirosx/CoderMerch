from django.shortcuts import render
from django.http import HttpRequest


def test_page(request: HttpRequest):
    return render(request, 'mainapp/test_page.html')

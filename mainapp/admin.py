from django.contrib import admin
from mainapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    """Диалог"""
    list_display = ('name', 'price', 'description', 'quantity', 'image')


admin.site.register(Product, ProductAdmin)

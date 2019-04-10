from django.contrib import admin
from mainapp.models import ProductCategory, Product, ProductBySize, ProductImage


# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductBySize)
admin.site.register(ProductImage)

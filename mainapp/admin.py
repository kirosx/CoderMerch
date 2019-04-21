from django.contrib import admin

from mainapp.models import *

admin.site.register(Product)
admin.site.register(ProductBySize)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)

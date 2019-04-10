from django.urls import path
from mainapp.views import ProductsList, ProductView, ProductCategory, ProductGender, ProductImg


app_name = 'mainapp'

urlpatterns = [
    # получение списка всех продуктов
    path('products/', ProductsList.as_view()),
    # получение данных одного продукта по первичному ключу
    path('product/<int:pk>/', ProductView.as_view()),
    # получение всех продуктов по категории
    path('products/category/<str:category>/', ProductCategory.as_view()),
    # получение всех продуктов по полу
    path('products/gender/<str:gender>/', ProductGender.as_view()),



]


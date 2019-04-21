

from rest_framework import routers
from mainapp.views import ProductViewSet, ProductCategoryViewSet

app_name = 'mainapp'

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', ProductCategoryViewSet)

urlpatterns = router.urls

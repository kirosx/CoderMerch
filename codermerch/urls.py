"""codermerch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from mainapp.views import ProductViewSet, ProductCategoryViewSet

from controllers import Views
from django.views.generic import RedirectView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', ProductCategoryViewSet)

urlpatterns = [
    path('', Views.HomeView.as_view(), name='home'),
    path('about/', Views.AboutView.as_view(), name='about'),
    path('products/', Views.ProductsView.as_view(), name='products'),
    path('product/', Views.ProductView.as_view(), name='product'),
    # path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls', namespace='api')),
    path('accounts/', include('allauth.urls')),
    path('favicon.ico',
         RedirectView.as_view(url='/static/img/favicon.png'),
         name='favicon'),
    path('api/v1/', include('mainapp.urls', namespace='models')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

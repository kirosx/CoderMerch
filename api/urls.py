from django.urls import include, path

from . import views
from api.views import CustomLogin

app_name = 'api'

urlpatterns = [
    path('', views.api_root),
    path('login/', CustomLogin.as_view(), name='rest_login'),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]

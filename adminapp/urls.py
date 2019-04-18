from django.urls import include, path

from . import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users'),
]

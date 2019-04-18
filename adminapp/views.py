from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from users.models import CustomUserManager


class UsersListView(ListView):
    model = CustomUserManager
    template_name = 'users.html'

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super(UsersListView, self).dispatch(*args, **kwargs)

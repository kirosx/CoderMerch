from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_auth.views import LoginView


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'login': reverse('api:rest_login', request=request, format=format),
        'logout': reverse('api:rest_logout', request=request, format=format),
        'register': reverse('api:rest_register', request=request,
                            format=format),
        'password reset': reverse('api:rest_password_reset', request=request,
                                  format=format),
        'password change': reverse('api:rest_password_change', request=request,
                                   format=format),
        'user details': reverse('api:rest_user_details', request=request,
                                format=format),
	'products': reverse('models:product-list', request=request, format=format),
        'categories': reverse('models:productcategory-list', request=request, format=format),
    })


class CustomLogin(LoginView):

    def get_response(self):
        orginal_response = super().get_response()
        print(self.request.POST.get('remember_me', 'false'))
        if self.request.POST.get('remember_me', 'false') == 'false':
            self.request.session.set_expiry(0)
        return orginal_response

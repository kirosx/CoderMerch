from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ProductsView(TemplateView):
    template_name = 'products.html'


class ProductView(TemplateView):
    template_name = 'product.html'

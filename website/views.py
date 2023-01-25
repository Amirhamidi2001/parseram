from django.views.generic.base import TemplateView


class CatView(TemplateView):
    template_name = "website/cat.html"


class ProductView(TemplateView):
    template_name = "website/product.html"

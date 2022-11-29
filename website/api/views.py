from rest_framework import viewsets

from ..models import Category, Product
from .serializers import CatSerializer, ProductSerializer
from .paginations import DefaultPagination


class CatViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving category.
    """
    serializer_class = CatSerializer
    queryset = Category.objects.all()
    pagination_class = DefaultPagination


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Product.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = DefaultPagination

from rest_framework import viewsets

from ..models import *
from .serializers import *
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


class CustomerViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Customer.
    """

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = DefaultPagination


class OrderDetailViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving OrderDetai.
    """

    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()
    pagination_class = DefaultPagination


class OrderViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving OrderDetai.
    """

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    pagination_class = DefaultPagination

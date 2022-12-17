from rest_framework import serializers

from ..models import *


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title", "parent"]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "id", "title", "image", "content", "category", "description"
            ]


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            "id", "name", "family", "address", "age", "city", "gender"
            ]


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = [
            "id", "o", "product", "quantity", "price"
            ]


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            "id", "user", "date", "totalprice"
            ]

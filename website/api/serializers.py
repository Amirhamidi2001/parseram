from rest_framework import serializers

from ..models import Category, Product


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title", "parent"]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "id", "name", "image", "content", "category", "description"
            ]

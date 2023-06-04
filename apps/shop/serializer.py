from rest_framework import serializers

from apps.shop.models import Category, Product, SubProduct


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields= "__all__"


class SubproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProduct
        fields="__all__"

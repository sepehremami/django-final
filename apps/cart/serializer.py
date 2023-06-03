from rest_framework import serializers

from apps.shop.models import CartItem 
from .models import OrderInfo, OrderItem, CategoryDiscount, ProductDiscount


class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class CategoryDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDiscount
        fields = ('category','discount_value','discount_unit','description','valid_until','expired','minimum_order_value','maximum_discount_amount')


class ProductDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDiscount
        fields = ('product', 'discount_value','discount_unit','description','valid_until','expired','minimum_order_value','maximum_discount_amount')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model:CartItem
        fields="__all__"
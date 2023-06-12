from rest_framework import serializers
from apps.shop.serializer import SubproductSerializer, ProductSerializer, CategorySerializer
from apps.shop.models import CartItem 
from .models import OrderInfo, OrderItem, CategoryDiscount, ProductDiscount
from apps.user.serializers import UserSerializer, AddressSerializer
from apps.user.models import User, Address





class AddressFiled(serializers.RelatedField):
    def get_queryset(self):
        return Address.objects.all()
    
    def to_representation(self, value):
        return AddressSerializer(value).data

    def to_internal_value(self, data):
        return data.get('id')


class Userfield(serializers.RelatedField):
    def get_queryset(self):
        return User.objects.all()

    def to_representation(self, value):
        return UserSerializer(value).data

    def to_internal_value(self, data):
        return data.get('id')

class OrderField(serializers.RelatedField):
    def get_queryset(self):
        return OrderInfo.objects.all()

    def to_representation(self, value):
        return OrderInfoSerializer(value).data

    def to_internal_value(self, data):
        return int(data.get('id'))


class OrderInfoSerializer(serializers.ModelSerializer):
    addr = AddressFiled()
    user = Userfield(queryset=User.objects.all())


    class Meta:
        model = OrderInfo
        fields = "__all__"

class OrderInfoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderField()
    product = SubproductSerializer()

    class Meta:
        model = OrderItem
        fields = "__all__"




class OrderItemPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["product"]


class CategoryDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDiscount
        fields = ('category','discount_value','discount_unit','description','valid_until','expired','minimum_order_value','maximum_discount_amount')
        depth=1


class ProductDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDiscount
        fields = ('product', 'discount_value','discount_unit','description','valid_until','expired','minimum_order_value','maximum_discount_amount')
        depth=1


class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model=CartItem
        fields="__all__"
        depth=1


class CartSpecialSerailizer(serializers.Serializer):
    product_id = serializers.CharField()
    price = serializers.CharField()
    quantity = serializers.CharField()
    

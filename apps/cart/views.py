from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from apps.shop.models import SubProduct
from apps.shop.models import Product
from rest_framework import viewsets
from .serializer import OrderInfoSerializer, OrderItemSerializer, ProductDiscountSerializer, CategoryDiscountSerializer
from .models import OrderInfo, OrderItem, ProductDiscount, CategoryDiscount
from rest_framework import permissions


@login_required(login_url='user/login')
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cache.set('cart', product, timeout=50)
    print(cache.get('cart'))
    return HttpResponse(cache.get("cart"))


class OrderInfoViewSet(viewsets.ModelViewSet):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializer
    permission_classes =[permissions.IsAuthenticated]



class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes =[permissions.IsAuthenticated]



class ProductDiscountViewSet(viewsets.ModelViewSet):
    queryset = ProductDiscount.objects.all()
    serializer_class = ProductDiscountSerializer
    permission_classes =[permissions.IsAuthenticated]


class CategoryDiscountViewSet(viewsets.ModelViewSet):
    queryset = CategoryDiscount.objects.all()
    serializer_class = CategoryDiscountSerializer
    permission_classes =[permissions.IsAuthenticated]


from django.views.generic import FormView
from django.urls import reverse_lazy
from rest_framework import generics
from apps.shop.models import CartItem
from .serializer import CartItemSerializer
from .models import OrderInfo


class AddToCartViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        a = CartItem
        user = self.request.user
        cart = OrderInfo.objects.select_related().filter(user=user)
        cartitem = CartItem.objects.filter(cart__user=user)
        return cartitem 




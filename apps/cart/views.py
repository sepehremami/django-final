from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from apps.shop.models import SubProduct
from apps.shop.models import Product
from rest_framework import viewsets
from .serializer import OrderInfoSerializer, OrderItemSerializer, ProductDiscountSerializer, CategoryDiscountSerializer, OrderInfoPostSerializer, OrderItemPostSerializer
from .models import OrderInfo, OrderItem, ProductDiscount, CategoryDiscount
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

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
    permission_classes =[permissions.AllowAny]

    def get_serializer_class(self, *args, **kwargs):
        OrderItemPostSerializer.label = 'order-item-post'
        OrderItemSerializer.label = 'order'
        if self.action == 'create':
            return OrderItemPostSerializer
        return OrderItemSerializer
    


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProductDiscountViewSet(viewsets.ModelViewSet):
    queryset = ProductDiscount.objects.all()
    serializer_class = ProductDiscountSerializer
    permission_classes =[permissions.IsAuthenticated]


class CategoryDiscountViewSet(viewsets.ModelViewSet):
    queryset = CategoryDiscount.objects.all()
    serializer_class = CategoryDiscountSerializer
    permission_classes =[permissions.IsAuthenticated]


from apps.shop.models import CartItem
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied


def cart_view(request):
    return render(request, 'cart/cart.html')


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_users_cart_items(request):
    user = request.user
    print(request.user)
    cart = get_object_or_404(OrderInfo, user=user)
    cart_items = OrderItem.objects.filter(order=cart)
    serializer = OrderItemSerializer(cart_items, many=True)
    return Response({'cart_items':serializer.data})

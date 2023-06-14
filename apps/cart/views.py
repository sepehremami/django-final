from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from apps.shop.models import SubProduct
from apps.shop.models import Product
from rest_framework import viewsets
from .serializer import CartDiscountSerializer, OrderInfoSerializer, OrderItemSerializer, ProductDiscountSerializer, CategoryDiscountSerializer, OrderInfoPostSerializer, OrderItemPostSerializer
from .models import CartDiscount, OrderInfo, OrderItem, ProductDiscount, CategoryDiscount
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

@login_required(login_url='user/login')
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cache.set('cart', product, timeout=50)
    return HttpResponse(cache.get("cart"))


class OrderInfoViewSet(viewsets.ModelViewSet):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializer
    permission_classes =[permissions.IsAuthenticated]




class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    permission_classes =[permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        product = self.request.data.get('product')
        count = int(self.request.data.get('count'))
        user = request.user
        
        try:
            order = OrderInfo.objects.get(user=request.user, order_status=2)
        except Exception:
            order = OrderInfo.objects.create(user=self.request.user, order_status=2)

        print(order)
        order_item, created = OrderItem.objects.get_or_create(order=order, product_id=product)
        if created:
            order_item.count = count
        else:
            order_item.count += count
        order_item.save()
        serializer_class = self.get_serializer_class()
        serialized_data = serializer_class(instance=order_item).data
        return Response(serialized_data,status=status.HTTP_201_CREATED,content_type='application/json')

    def get_serializer_class(self, *args, **kwargs):
        OrderItemPostSerializer.label = 'order-item-post'
        OrderItemSerializer.label = 'order'
        if self.action == 'create':
            return OrderItemPostSerializer
        return OrderItemSerializer
    



class ProductDiscountViewSet(viewsets.ModelViewSet):
    queryset = ProductDiscount.objects.filter(is_deleted=False)
    serializer_class = ProductDiscountSerializer
    permission_classes =[permissions.IsAuthenticated]


class CategoryDiscountViewSet(viewsets.ModelViewSet):
    queryset = CategoryDiscount.objects.filter(is_deleted=False)
    serializer_class = CategoryDiscountSerializer
    permission_classes =[permissions.IsAuthenticated]


class CartDiscountViewSet(viewsets.ModelViewSet):
    queryset = CartDiscount.objects.filter(is_deleted=False)
    serializer_class = CartDiscountSerializer
    permission_classes = [permissions.IsAuthenticated]

from apps.shop.models import CartItem
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied


def cart_view(request):
    return render(request, 'cart/cart.html')

from django.views.generic import TemplateView, DetailView
from apps.user.views import AuthenticationRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


class CartTemplateView(TemplateView):
    model = OrderInfo
    template_name = 'cart/cart.html'

    def get(self, request , *args, **kwargs):

        user = self.request.user
        try:
            order_info = OrderInfo.objects.get(pk=kwargs.get('pk'))
            if order_info.user != user:
                return redirect(reverse('landing'))
        except:
            pass

        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):  
        user = self.request.user  
        if not user.is_authenticated:
            pass
            # return redirect('landing')
    
        user = self.request.user
        id = self.request.COOKIES.get('id')
        print(id)
        context = super().get_context_data(**kwargs)
        order_id = self.request.session.get('order_id')
        print(order_id)
        try:
            cart = OrderInfo.objects.get(id=int(kwargs.get('pk')))
            
            # If cart already belongs to authenticated User then proceed further otherwise raise some custom exception or redirect back.
            if user == cart.user: 
                context['cart'] = cart
                
            # Redirecting back incase Cart doesn't belong to current authenticated User instance.
            else:     
                return redirect("some_redirect_url")
            
        except (ObjectDoesNotExist, IntegrityError):
          # If Cart doesn't exist with given id(pk) value then create new one for Authenticated User Instance.
            # cart = OrderInfo.objects.create(user=user, order_status=2)      
            # context['cart'] = cart
            pass
        return context


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_users_cart_items(request):
    user = request.user
    cart = get_object_or_404(OrderInfo, user=user)
    cart_items = OrderItem.objects.filter(order=cart)
    serializer = OrderItemSerializer(cart_items, many=True)
    return Response({'cart_items':serializer.data})


from .serializer import CartSpecialSerailizer

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def final_order(request):

    datas = request.data
    order_items = []
    prices = []
    for data in datas:
        product_id = data.get('product_id')
        price = int(data.get('price'))
        quantity = int(data.get('quantity'))
        total_price = price * quantity
        prices.append(total_price)
        get_subproduct = SubProduct.objects.get(id=product_id)
        order_items.append(get_subproduct)
    print(prices)
    print(order_items)



    return Response({'hi':'hi'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def validate_discount(request, *args, **kwargs):
    code = kwargs.get('code')
    print(code)

    discount = CartDiscount.objects.get(code=code)
    serializer = CartDiscountSerializer(instance=discount)
    return Response(serializer.data)

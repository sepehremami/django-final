from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.cache import cache

from apps.shop.models import Product


def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cache.set('cart', product, timeout=50)
    print(cache.get('cart'))

from django.shortcuts import render
from apps.shop.models import Product, Category


def home(request):
    category = Category.objects.all()
    products = Product.objects.all()[:6]
    return render(request, 'landing.html', {'products': products, 'category':category})



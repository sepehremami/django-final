from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, DetailView

from .forms import ProductForm
from .models import Product

from django.views.generic.edit import CreateView
from apps.shop.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "shop/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['product.add_product']
    model = Product
    login_url = '/accounts/login'
    fields = "__all__"



@login_required(login_url='/accounts/login')
def wishlist(request):
    return HttpResponse('added')

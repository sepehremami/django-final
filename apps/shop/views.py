from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, DetailView
from django.core.cache import cache
from .forms import ProductForm
from .models import Product, Category

from django.views.generic.edit import CreateView
from apps.shop.models import Product
from django.db.models import Q

class CategoryMixin:
    def get_context_data(self, **kwargs):
        context = super(CategoryMixin, self).get_context_data(**kwargs)
        context['navbar_categories'] = Category.objects.filter(parent__isnull=True)
        return context


def load_category_globally(request):
    category = Category.objects.all()
    return {'category':category}

class ProductListView(CategoryMixin, ListView):
    model = Product
    template_name = "shop/product_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        best = Product.objects.all()
        context['best_sellers'] = best
        return context

    def get_queryset(self):
        query = self.request.GET.get("product")
        print(query)
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(desc__icontains=query)
        )
        return object_list


class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["shopping_cart"] = cache.get("cart")
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ["product.add_product"]
    model = Product
    login_url = "/accounts/login"
    fields = "__all__"


@login_required(login_url="/accounts/login")
def wishlist(request):
    return HttpResponse("added")


class CategoryListView(CategoryMixin, ListView):
    model = Category
    template_name = 'shop/category_list.html'
    context_object_name = 'categories'


    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(parent__isnull=True)


class CategoryDetailView(CategoryMixin, DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
    context_object_name = 'category_detail'

    def get(self, request, *args, **kwargs):
        parent = super().get(self, request,*args, **kwargs)
        return parent

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(self)
        cateogry = Category.objects.get(pk=int(kwargs.get('pk')))
        product = Product.objects.filter()
        context['product'] = product
        return context
        



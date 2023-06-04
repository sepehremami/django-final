from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, TemplateView, DetailView
from django.core.cache import cache
from .forms import ProductForm
from .models import Media, Product, Category, SubProduct
from django.db.models import F
from django.views.generic.edit import CreateView
from apps.shop.models import Product
from django.db.models import Q

def load_category_globally(request):
    category = Category.objects.filter(parent__isnull=True)
    return {'category':category}

class CategoryMixin:
    def get_context_data(self, **kwargs):
        context = super(CategoryMixin, self).get_context_data(**kwargs)
        context['navbar_categories'] = Category.objects.filter(parent__isnull=True)
        return context


class ProductListView(ListView):
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

class ProductDetailView(TemplateView):
    model = Product
    template_name = "shop/product_detail.html"
    

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs.get('pk'))
        context['product'] = product
        subproducts = SubProduct.objects.filter(product=product)
        # for sub in subproducts:
        #     sub.objects.annotate(price= F("pricing__price")).filter(price__is_active=True).values('id', 'name', 'desc', 'stock', 'price')
        context['subs'] = subproducts
        list_image =[]
        for sub in subproducts:
            for image in sub.media_set.all():
                list_image.append(image)

        context['images'] = list_image
        return context



class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ["product.add_product"]
    model = Product
    login_url = "/accounts/login"
    fields = "__all__"


@login_required(login_url="/accounts/login")
def wishlist(request):
    return HttpResponse("added")


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category_list.html'
    context_object_name = 'categories'


    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(parent__isnull=True)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
    context_object_name = 'category_detail'

    def get(self, request, *args, **kwargs):
        parent = super().get(self, request,*args, **kwargs)
        return parent

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        cateogry = Category.objects.get(pk=int(self.kwargs.get('pk')))
        product = Product.objects.filter(category=cateogry)
        context['products'] = product
        return context
        



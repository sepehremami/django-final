from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, TemplateView, DetailView
from django.core.cache import cache
from apps.cart.models import OrderInfo, OrderItem
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

from django.shortcuts import redirect
from django.contrib import messages
from .models import Pricing
from plotly.offline import plot
import plotly.graph_objs as go

class ProductDetailView(TemplateView):
    model = Product
    template_name = "shop/product_detail.html"

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs.get('pk'))
        subproduct = SubProduct.objects.filter(product=product).first()
        pricing_data = Pricing.objects.filter(subproduct=subproduct).order_by('create_date')

        # plotly
        trace = go.Scatter(x=[p.create_date for p in pricing_data], y=[p.price for p in pricing_data])
        layout = go.Layout(title='Price over Time', xaxis=dict(title='Date'), yaxis=dict(title='Price'))
        fig = go.Figure(data=[trace], layout=layout)

        graph = fig.to_html(full_html=True, default_height=500, default_width=700)
        context = self.get_context_data()
        context['chart'] = graph
        return render(self.request, 'shop/product_detail.html', context)

    def post(self, request,*args, **kwargs):
        price = self.request.POST.get('price')
        try:
            subid = int(self.request.POST.get('id'))
            count = int(self.request.POST.get('count'))
        except Exception as e: 
            messages.error(self.request,'something went wrong')
            return render(self.request, 'shop/product_detail.html')
        
        try:
            cart, created = OrderInfo.objects.get_or_create(user=self.request.user, order_status=2)
            order_item, created = OrderItem.objects.get_or_create(product_id=subid, order=cart)
        except Exception as e:
            print(e)
        # subproduct = SubProduct.objects.get(id=id)
        
        print(order_item)
        if created:
            order_item.count = count
        else:
            order_item.count += count

        order_item.save()
        self.request.session['order_id'] = cart.id
        messages.success(request,"Your item has been added to cart.")
        context = self.get_context_data()
        return render(self.request, 'shop/product_detail.html', context)


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
        


from django.shortcuts import render
from apps.shop.models import Product, Category
from django.views.generic import TemplateView
from apps.shop.views import CategoryMixin
def home(request):
    category = Category.objects.all()
    products = Product.objects.all()[:6]
    return render(request, 'landing.html', {'products': products, 'category':category})


class HomeView(CategoryMixin, TemplateView):
    template_name= 'landing.html'

    def get(self, *args, **kwargs):
        category = Category.objects.all()
        products = Product.objects.all()[:6]
        return render(request=self.request, template_name='landing.html', context={'products': products, 'category':category})


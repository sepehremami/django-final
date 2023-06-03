from django.shortcuts import render
from apps.shop.models import Product, Category
from django.views.generic import TemplateView
from apps.shop.views import CategoryMixin
from apps.user.models import User

from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    category = Category.objects.all()
    products = Product.objects.all()[:6]
    return render(request, 'landing.html', {'products': products, 'category':category})


class HomeView(CategoryMixin, TemplateView):
    template_name= 'landing.html'

    def get(self, *args, **kwargs):
        category = Category.objects.all()
        products = Product.objects.all()[:6]
        best = Product.objects.all()[:3]
        return render(request=self.request, template_name='landing.html', 
        context={'products': products, 'category':category, 'best_sellers':best})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best_sellers'] = Product.objects.all()
        return context


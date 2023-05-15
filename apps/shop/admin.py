from django.contrib import admin
from .models import Product, Cart, CartItem, Category, ShoppingSession

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(ShoppingSession)

from django.contrib import admin
from .models import Product, Cart, CartItem, Category, ShoppingSession, Media, Dummy
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


# class ProductAdmin(admin.ModelAdmin):
#     list_filter = (
#         ("create_at", JDateFieldListFilter),
#     )

class DummyAdmin(admin.ModelAdmin):
    list_filter = (("dummy_date", JDateFieldListFilter),)


admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(ShoppingSession)
admin.site.register(Media)
admin.site.register(Dummy, DummyAdmin)

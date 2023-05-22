from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


class ProductAdmin(admin.ModelAdmin):
    list_filter = (("create_at", JDateFieldListFilter),)


admin.site.register(Pricing)
admin.site.register(ProductColour)
admin.site.register(SubProduct)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Media)
admin.site.register(ProductReview)

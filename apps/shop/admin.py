from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


class SubProductInline(admin.TabularInline):
    model = SubProduct


class SubCategoryInline(admin.TabularInline):
    model = Category
    fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = (("create_date", JDateFieldListFilter),)
    fieldsets = (
        ("general", {"fields": ("name", 'category')}),
        ("other", {"fields": ("desc", 'image')}),
    )
    inlines = (SubProductInline,)


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (SubCategoryInline,)


admin.site.register(ProductColour)
admin.site.register(SubProduct)

admin.site.register(CartItem)
admin.site.register(Media)
admin.site.register(ProductReview)

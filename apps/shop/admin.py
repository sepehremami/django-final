from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin
from django.utils.text import Truncator
from django.utils.html import format_html
from django.forms.models import inlineformset_factory
from .forms import MediaForm
from easy_thumbnails.templatetags.thumbnail import thumbnail_url


class PricingInline(admin.TabularInline):
    model = Pricing



class MediaInline(admin.TabularInline):
    model = Media
    form = MediaForm
                                     

class SubProductInline(admin.TabularInline):
    model = SubProduct


class SubCategoryInline(admin.TabularInline):
    model = Category
    fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "short_description", "category", "image_tag")
    list_filter = (("create_date", JDateFieldListFilter),)
    fieldsets = (
        ("general", {"fields": ("name", "category")}),
        ("other", {"fields": ("desc", "image")}),
    )
    inlines = (SubProductInline,)

    def short_description(self, obj):
        return Truncator(obj.desc).words(
            25
        )  # Use Truncator class and call words() method with desired word


    def image_tag(self, obj):
            thumbnail = thumbnail_url(obj.image, 'thumbnail')
            return format_html('<img src="{}" width="50"/>'.format(thumbnail))


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ["subproduct", "price", "is_active"]
    list_filter = ["is_active"]
    date_hierarchy = "create_date"

    fieldsets = (
        (None, {"fields": ("subproduct", "price")}),
        ("Last Price", {"fields": ("is_active",)}),
    )


@admin.register(SubProduct)
class SubprodctAdmin(admin.ModelAdmin):
    list_display = ["product", "sku", "size", "colour", "stock"]
    inlines = [PricingInline, MediaInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent' ,'name' ,'short_desc' ,'image_tag']
    inlines = (SubCategoryInline,)

    def short_desc(self, obj):
        return Truncator(obj.desc).words(
            25
        ) 
        
    def image_tag(self, obj):
            thumbnail = thumbnail_url(obj.image, 'thumbnail')
            return format_html('<img src="{}" width="50"/>'.format(thumbnail))



@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("name", "subproduct", "image_tag")

    def image_tag(self, obj):
        thumbnail = thumbnail_url(obj.img, 'thumbnail')
        return format_html('<img src="{}" width="50"/>'.format(thumbnail))

admin.site.register(ProductColour)
admin.site.register(CartItem)
admin.site.register(ProductReview)


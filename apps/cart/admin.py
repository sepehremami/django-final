from django.contrib import admin
from .models import *


@admin.register(CategoryDiscount)
class CategoryDiscountAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "discount_value",
        "discount_unit",
        "valid_until",
        "expired",
        "minimum_order_value",
        "maximum_discount_amount",
        "category",
    ]


@admin.register(CartDiscount)
class CartDiscountAmin(admin.ModelAdmin):
    list_display = (
        "id",
        "code",
        "discount_value",
        "discount_unit",
        "valid_until",
        "expired",
        "minimum_order_value",
        "maximum_discount_amount",
        "order",
    )


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = [
        "discount_value",
        "discount_unit",
        "valid_until",
        "expired",
        "minimum_order_value",
        "maximum_discount_amount",
        "product",
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "count"]


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "addr", "total_count", "total_price", "order_status"]

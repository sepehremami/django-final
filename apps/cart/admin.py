from django.contrib import admin
from .models import *


admin.site.register(OrderInfo)
admin.site.register(OrderItem)
admin.site.register(CategoryDiscount)
admin.site.register(ProductDiscount)


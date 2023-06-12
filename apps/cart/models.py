import uuid
from django_jalali.db import models as jmodels
from django.db import models
from django.db import models
from apps.core.models import BaseModel
from apps.user.models import User, Address
from .managers import OrderInfoManager

class OrderInfo(BaseModel):
    """
    order instance save user's orders
    """
    ORDER_STATUS = {
        1: 'done',
        2: 'not_done',
    }

    ORDER_STATUS_CHOICES = (
        (1, 'done'),
        (2, 'not done'),

    )

    order_id = models.UUIDField(unique=True, default=uuid.uuid4(), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    addr = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True )
    total_count = models.IntegerField(default=1, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, blank=True, null=True)


    def __str__(self) -> str:
        return f'{self.order_id}'


class OrderItem(BaseModel):
    """
    Order item is each Sub-product user buys
    """
    order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey('shop.SubProduct', on_delete=models.CASCADE)
    count = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.product.product.name}'


class DiscountBase(BaseModel):
    """
    All discount models inherit from this Base model
    """
    discount_value = models.IntegerField()
    discount_unit = models.CharField(max_length=1, choices=[
        ('t', 'Toman'),
        ('p', 'Percent'),
    ])
    description = models.TextField()
    valid_until = jmodels.jDateTimeField()
    expired = models.BooleanField(default=False)
    minimum_order_value = models.IntegerField()
    maximum_discount_amount = models.IntegerField()

    class Meta:
        abstract = True


class CategoryDiscount(DiscountBase):
    """
    this specific kind of discount can be applied to a category of products
    """
    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE, related_name='discount')


class ProductDiscount(DiscountBase):
    """
    this specific kind of discount is applied only on one Sub-product
    """
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='discount')

# TODO: WISHLIST implementation
# TODO: Fix Eternal Migration Loop

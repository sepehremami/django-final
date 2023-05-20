import uuid
from django_jalali.db import models as jmodels
from django.db import models
from django.db import models
from apps.core.models import BaseModel
from apps.user.models import User, Address
class OrderInfo(BaseModel):
    """
    order instance save user's orders
    """
    ORDER_STATUS = {
        1: 'paid',
        2: 'shipped',
        3: 'received',
        4: 'evaluated',
        5: 'Completed',
    }

    ORDER_STATUS_CHOICES = (
        (1, 'paid'),
        (2, 'shipped'),
        (3, 'received'),
        (4, 'evaluated'),
        (5, 'Completed')
    )

    order_id = models.UUIDField(default=uuid.uuid4(), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    addr = models.ForeignKey(Address, on_delete=models.CASCADE, )
    total_count = models.IntegerField(default=1, editable=False )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, )


class OrderItem(BaseModel):
    """
    Order item is each Sub-product user buys
    """
    order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE)
    sku = models.ForeignKey('shop.SubProduct', on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class DiscountBase(BaseModel):
    """
    All discount models inherit from this Base model
    """
    coupon_code = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50,
                                   editable=False)
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
    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE)


class ProductDiscount(DiscountBase):
    """
    this specific kind of discount is applied only on one Sub-product
    """
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)

# TODO:WISHLIST implementation

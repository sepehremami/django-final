from django.db import models
from django.db import models
from apps.core.models import BaseModel, User, Address
from apps.shop.models import Product, SubProduct


class OrderInfo(BaseModel):
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

    order_id = models.CharField(max_length=128, primary_key=True, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    addr = models.ForeignKey(Address, on_delete=models.CASCADE, )
    total_count = models.IntegerField(default=1, )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, )
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, )
    trade_no = models.CharField(max_length=128, default='', )


class OrderGoods(BaseModel):
    order = models.ForeignKey('OrderInfo', on_delete='CASCADE')
    sku = models.ForeignKey(SubProduct.sku, on_delete='CASCADE')
    count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=256, default='')


class Discount(BaseModel):
    discount_value = models.IntegerField()
    discount_unit = models.CharField(choices=[
        ('t', 'Toman'),
        ('p', 'Percent'),
    ])
    description = models.TextField()
    valid_until = models.DateTimeField()
    expired = models.BooleanField(default=False)

    class Meta:
        abstract = True

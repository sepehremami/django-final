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

    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    addr = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True )
    total_count = models.IntegerField(default=1, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, blank=True, null=True)
    objects = OrderInfoManager()


    def __str__(self) -> str:
        return f'{self.order_id}'


    def get_total_count(self):
        count = self.order_item.aggregate(models.Sum('count'))['count__sum']
        return count or 0

    def get_total_price(self):
        total_price = 0
        for item in self.order_item.all():
            print(item)
            total_price += item.cal_price()
        return total_price


class OrderItem(BaseModel):
    """
    Order item is each Sub-product user buys
    """
    order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey('shop.SubProduct', on_delete=models.CASCADE)
    count = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.product.product.name}'

    def cal_price(self):
        price = self.product.get_active_price().price
        total_price = price * self.count
        return total_price

    def save(self, *args, **kwargs):
        order = OrderItem.objects.get(pk=self.pk).count
        self.order.total_count += self.count - order
        self.order.save()
        super(OrderItem, self).save(*args, **kwargs)

    


class DiscountBase(BaseModel):
    """
    All discount models inherit from this Base model
    """
    code = models.CharField(max_length=5, blank=True)
    discount_value = models.DecimalField(decimal_places=2,  max_digits=8)
    discount_unit = models.CharField(max_length=1, choices=[
        ('t', 'Toman'),
        ('p', 'Percent'),
    ])
    description = models.TextField(null=True, blank=True)
    valid_until = jmodels.jDateTimeField(null=True, blank=True)
    expired = models.BooleanField(default=False)
    minimum_order_value = models.IntegerField(null=True, blank=True)
    maximum_discount_amount = models.IntegerField(null=True, blank=True)

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

class CartDiscount(DiscountBase):
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, related_name='discount')




            
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

@receiver(pre_save, sender=CartDiscount)
def generate_discount_code(sender, instance=None, **kwargs):
    """
    Signal handler to generate random 5 digit code for each Discount object.
    """
    
    if not instance.pk:
        # Generate new discount code only when creating a new object.
        from random import randint
        base_code = str(randint(10000, 99999))
        
        # Ensure no other existing Discount objects have the same code.
        while CartDiscount.objects.filter(code=base_code).exists():
            base_code = str(randint(10000, 99999))

        instance.code = base_code
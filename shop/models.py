from django.db import models
from core.models import BaseModel, User

class ShoppingSession(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(null=True, blank=True)

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=500)
    status = models.smalint


class Product(BaseModel):
    name = models.CharField(max_length=150)
    desc = models.TextField()
    sku = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True, blank=True)
    price = models.DecimalField()
    discount = models.ForeignKey('Discount', on_delete=models.RESTRICT, null=True, blank=True)



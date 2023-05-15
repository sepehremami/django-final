from django.db import models
from core.models import BaseModel, User


class ShoppingSession(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=500)
    status = models.CharField(
        max_length=3,
        choices=[
            ("A", "Available"),
            ("U", "Unavailable"),
        ],
        default="U",
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class Category(BaseModel):
    name = models.CharField(max_length=100)
    desc = models.TextField()


class Product(BaseModel):
    name = models.CharField(max_length=150)
    desc = models.TextField()
    sku = models.CharField(max_length=100)
    category = models.ForeignKey(
        "Category", on_delete=models.RESTRICT, null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.ForeignKey(
        "Discount", on_delete=models.RESTRICT, null=True, blank=True
    )


class CartItem(BaseModel):
    cart = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.RESTRICT)
    quantity = models.SmallIntegerField()

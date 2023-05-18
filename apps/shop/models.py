from django.db import models
from django.urls import reverse
from apps.core.models import BaseModel, User
from profanity.validators import validate_is_profane
from django_jalali.db import models as jmodels


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

    def __str__(self) -> str:
        return f"{self.user.email}'s + Cart"  # type:ignore


class Category(BaseModel):
    name = models.CharField(max_length=100)
    desc = models.TextField(validators=[validate_is_profane])

    def __str__(self) -> str:
        return f"{self.name}"


class Product(BaseModel):
    name = models.CharField(max_length=150)
    desc = models.TextField(validators=[validate_is_profane])
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("product-detail", args=[str(self.pk)])


class SubProduct(BaseModel):
    product_size = [
        ('s', 'Small'),
        ('m', 'Medium'),
        ('l', 'Large'),
        ('xl', 'Extra-Large'),
        ('xxl', '2Extra-Large')
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length=100)
    size = models.CharField(max_length=5, choices=product_size)
    colour = models.ForeignKey("ProductColour", on_delete=models.RESTRICT)
    suppliers_price = models.IntegerField()
    retail_price = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.ForeignKey(
        "Discount", on_delete=models.RESTRICT, null=True, blank=True
    )


class ProductColour(BaseModel):
    colour = models.CharField(max_length=50)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.RESTRICT)
    quantity = models.SmallIntegerField()

    def __str__(self) -> str:
        return f"{self.product.name}"


class Discount(BaseModel):
    name = models.CharField(max_length=100)
    desc = models.TextField(validators=[validate_is_profane])
    discount_percent = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"


class Media(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images", null=True, blank=True)


class Dummy(models.Model):
    dummy_date = jmodels.jDateTimeField()

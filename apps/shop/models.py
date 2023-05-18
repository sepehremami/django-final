from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from apps.core.models import BaseModel, User
from profanity.validators import validate_is_profane
from django_jalali.db import models as jmodels
from apps.cart.models import CategoryDiscount, ProductDiscount


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
    parent_id = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, blank=True, editable=False)
    name = models.CharField(max_length=100)
    desc = models.TextField(validators=[validate_is_profane])
    image = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Product(BaseModel):
    name = models.CharField(max_length=150)
    desc = models.TextField(validators=[validate_is_profane])
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    class Meta:
        app_label = 'shop'

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("product-detail", args=[str(self.pk)])


class Pricing(BaseModel):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)


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
    price = models.ForeignKey(Pricing, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'shop'

    def size_verbose(self):
        return dict(SubProduct.product_size)[self.size]

    def __str__(self):
        return f"{self.product.name}"


class ProductColour(BaseModel):
    colour = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.colour}"


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.RESTRICT)
    quantity = models.SmallIntegerField()

    def __str__(self) -> str:
        return f"{self.product.name}"


class Media(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images", null=True, blank=True)


def validate_max_five(value):
    if 0 <= value <= 5:
        raise ValidationError(
            "%(value)s is not between 0 and 5",
            params={"value": value},)


class ProductReview(BaseModel):
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=5, decimal_places=0, validators=[validate_max_five])
    text = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user.username}:{self.product}:{self.pk}"

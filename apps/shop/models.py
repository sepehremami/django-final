from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import QuerySet
from django.db.models.functions import Greatest
from django.urls import reverse
from apps.core.models import BaseModel
from apps.user.models import User
from profanity.validators import validate_is_profane
from django_jalali.db import models as jmodels
from apps.cart.models import CategoryDiscount, ProductDiscount, OrderInfo


class Category(BaseModel):
    """
    self-relation
    product category
    """
    parent = models.ForeignKey('shop.Category', on_delete=models.RESTRICT, null=True, blank=True)
    name = models.CharField(max_length=100)
    desc = models.TextField(validators=[validate_is_profane])
    image = models.ImageField(upload_to="images", null=True, blank=True)

    def load_children(self):
        if self.category_set.all():
            return self.category_set.all()
        return False

    def parse_children(self):
        if isinstance((self.load_children()), QuerySet):
            for category in self.load_children():
                yield category.name
        else:
            return None

    class Meta:
        app_label = "shop"

    def __str__(self) -> str:
        return f"{self.name}"


class Product(BaseModel):
    """
    Products are the core reason we are writing this django website
    """
    name = models.CharField(max_length=150)
    desc = models.TextField(validators=[validate_is_profane])
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    image = models.ImageField(null=True)

    class Meta:
        app_label = 'shop'

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("product-detail", args=[str(self.pk)])


class Pricing(BaseModel):
    """
    pricing is defined for better control over price behaviour
    """
    subproduct = models.ForeignKey('shop.SubProduct', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(verbose_name='Price of a Subproduct', null=True)
    is_active = models.BooleanField(default=True)

    def test(self):
        all_before_prices = self.subproduct.pricing_set.filter(subproduct__pricing=self)
        return all_before_prices

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()




    def __str__(self):
        return f'{self.price} id: {self.subproduct_id}'


class SubProduct(BaseModel):
    """
    Sub-products are essentially products but with more specific data on colour,
    size, price,...
    """
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
    image = models.ImageField

    class Meta:
        app_label = 'shop'

    def size_verbose(self):
        return dict(SubProduct.product_size)[self.size]

    def __str__(self):
        return f"{self.product.name}"


class ProductColour(BaseModel):
    """
    colour of products,
    split because of redundancy
    """
    colour = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.colour}"


class CartItem(BaseModel):
    """
    """
    cart = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, null=True)
    product = models.OneToOneField(Product, on_delete=models.RESTRICT)
    quantity = models.SmallIntegerField()

    def __str__(self) -> str:
        return f"{self.product.name}"


class Media(BaseModel):
    name = models.CharField(max_length=50, null=True)
    subproduct = models.ForeignKey(SubProduct, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to="media/media", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


def validate_max_five(value):
    if 0 <= value <= 5:
        raise ValidationError(
            "%(value)s is not between 0 and 5",
            params={"value": value}, )


class ProductReview(BaseModel):
    """
    user's product review
    """
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=5, decimal_places=0, validators=[validate_max_five])
    text = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user.username}:{self.product}:{self.pk}"

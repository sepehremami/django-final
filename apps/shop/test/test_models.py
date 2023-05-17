from django.test import TestCase
from apps.shop.models import Category, Discount, Product


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.discount = Discount.objects.create(name="Test Discount", discount_percent=10)
        self.product = Product.objects.create(
            name="Test Product",
            desc="Test Description",
            sku="12345",
            category=self.category,
            price=100,
            discount=self.discount,
        )

    def test_product_name(self):
        self.assertEqual(self.product.name, "Test Product")

    def test_product_desc(self):
        self.assertEqual(self.product.desc, "Test Description")

    def test_product_sku(self):
        self.assertEqual(self.product.sku, "12345")

    def test_product_category(self):
        self.assertEqual(self.product.category, self.category)

    def test_product_price(self):
        self.assertEqual(self.product.price, 100)

    def test_product_discount(self):
        self.assertEqual(self.product.discount, self.discount)

    def test_user_cannot_modify_product(self): ...

    def test_admin_can_modify_product(self): ...

    def test_staff_can_modify_product(self): ...

    def test_product_discount_works(self): ...

import pytest
from django.core.exceptions import ValidationError
from django.test import TestCase
from apps.shop.models import Product
from model_bakery import baker
from django.test import TestCase
from apps.shop.models import Category, Discount, Product





class ProductModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.discount = Discount.objects.create(
            name="Test Discount", discount_percent=10
        )
        self.product = Product.objects.create(
            name="Test Product",
            desc="Test Description",
            category=self.category,
        )

    @pytest.mark.django_db
    def test_product_name_length_constraint(self):
        error_case = 'a' * 151
        self.product.name = error_case
        with self.assertRaises(ValidationError):
            self.product.full_clean()

    @pytest.mark.django_db
    def test_product_desc(self):
        self.assertEqual(self.product.desc, "Test Description")

    def test_product_sku(self):
        self.assertEqual(self.product.sku, "12345")

    def test_product_category(self):
        self.assertEqual(self.product.category, self.category)


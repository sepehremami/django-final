from django.test import TestCase
from ..models import SubProduct, Product, ProductColour, Category, Pricing


class SubProductModelTest(TestCase):
    def setUp(self):
        # Create a ProductColour object for testing
        colour = ProductColour.objects.create(colour='Red')
        cat = Category.objects.create(name='t-shirt', desc='no desc')
        # Create a Product object for testing
        product = Product.objects.create(name='T-Shirt', desc='A comfortable t-shirt', category=cat)

        # Create a SubProduct object for testing
        subproduct = SubProduct.objects.create(product=product, sku='TS001', size='s', colour=colour)
        pricing = Pricing.objects.create(price=product, is_active=True)

    def test_size_verbose(self):
        subproduct = SubProduct.objects.get(id=1)
        self.assertEqual(subproduct.size_verbose(), 'Small')

    def test_str(self):
        subproduct = SubProduct.objects.get(id=1)
        self.assertEqual(str(subproduct), 'T-Shirt')

    def test_pricing_and_subproduct_relation(self):
        pricing = Pricing.objects.get(id=1)
        subproduct = SubProduct.objects.get(id=1)
        self.assertEqual(pricing.price, subproduct)

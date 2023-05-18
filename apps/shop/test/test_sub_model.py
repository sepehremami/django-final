from django.test import TestCase
from ..models import SubProduct, Product, ProductColour, Category

class SubProductModelTest(TestCase):
    def setUp(self):
        # Create a ProductColour object for testing
        colour = ProductColour.objects.create(colour='Red')
        cat = Category.objects.create(name='t-shirt', desc='no desc')
        # Create a Product object for testing
        product = Product.objects.create(name='T-Shirt', desc='A comfortable t-shirt', category=cat)

        # Create a SubProduct object for testing
        SubProduct.objects.create(product=product, sku='TS001', size='s', colour=colour)

    def test_size_verbose(self):
        subproduct = SubProduct.objects.get(id=1)
        self.assertEqual(subproduct.size_verbose(), 'Small')

    def test_str(self):
        subproduct = SubProduct.objects.get(id=1)
        self.assertEqual(str(subproduct), 'T-Shirt')

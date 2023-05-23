import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import OrderInfo, OrderItem, Address
import uuid
from ...shop.models import Category, Product, SubProduct, ProductColour

User = get_user_model()


def test_is_default_label():
    address = Address.objects.get(id=1)
    field_label = address


class ShopAppTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''
        populate the database
        '''
        user = User.objects.create_user(username='test-user', password='12345')
        address = Address.objects.create(user_id=1, receiver='John Doe', province='California', city='Los Angeles',
                                         addr='123 Main St', zip_code='12345', phone='555-555-5555', is_default=False)
        cat = Category.objects.create(name='t-shirt', desc='no desc')
        colour = ProductColour.objects.create(colour='Red')
        product = Product.objects.create(name='T-Shirt', desc='A comfortable t-shirt', category=cat)

        subproduct = SubProduct.objects.create(product=product, sku='TS001', size='s', colour=colour)
        order = OrderInfo.objects.create(user=user, addr=address, total_count=2, total_price=10.00, order_status=1)
        OrderItem.objects.create(order=order, sku=subproduct, count=1, price=5.00)

    def test_order_id(self):
        """
        set order id
        """
        order = OrderInfo.objects.get(id=1)
        self.assertIsInstance(order.order_id, uuid.UUID)

    def test_order_status_choices(self):
        """
        check order status
        """
        order = OrderInfo.objects.get(id=1)
        self.assertIn(order.order_status, [1, 2, 3, 4, 5])

    def test_total_count(self):
        """
        check total_count field
        """
        order = OrderInfo.objects.get(id=1)
        self.assertEqual(order.total_count, 2)

    def test_total_price(self):
        order = OrderInfo.objects.get(id=1)
        self.assertEqual(order.total_price, 10.00)

    def test_order_item_count(self):
        order_item = OrderItem.objects.all()
        self.assertEqual(order_item.count(), 1)

    def test_order_item_price(self):
        order_item = OrderItem.objects.get(id=1)
        self.assertEqual(order_item.price, 5.00)

    def test_user_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_receiver_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('receiver').verbose_name
        self.assertEqual(field_label, 'receiver')

    def test_province_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('province').verbose_name
        self.assertEqual(field_label, 'province')

    def test_city_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('city').verbose_name
        self.assertEqual(field_label, 'city')

    def test_addr_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('addr').verbose_name
        self.assertEqual(field_label, 'addr')

    def test_zip_code_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('zip_code').verbose_name
        self.assertEqual(field_label, 'zip code')

    def test_phone_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'phone')

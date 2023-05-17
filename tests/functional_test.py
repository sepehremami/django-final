from django.http import HttpRequest
from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from apps.shop.models import Product, Category
from apps.shop.views import ProductListView


class NewVisitorTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.category = Category.objects.first()
        self.new_product_obj = Product.objects.create(
            name="t-shirt",
            desc="beautiful",
            sku='111',
            category=self.category,
            price=12.99,
        ).save()
        self.product = Product.objects.get(name='t-shirt')
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_view_product_view(self):
        self.browser.get(f"{self.live_server_url}/product")

        self.assertIn(self.product.name, self.browser.page_source)

    # def test_can_make_a_product_and_retrieve(self):
    #     pass


class Homepage(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'shop/home.html')

from django.http import HttpRequest
from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from apps.shop.models import Product, Category
from apps.shop.views import ProductListView
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


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

    def wait_for_products_to_load(self, product_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id')
                products = table.find_elements(By.TAG_NAME, 'li')
                self.assertIn(product_text, [product.text for product in products])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def check_for_product_name_in_products(self, product_name):
        products = self.browser.find_elements(By.TAG_NAME, 'h4')
        products_names = [product.text for product in products]
        self.assertIn(self.product.name, self.browser.page_source)

    def test_can_view_product_view(self):
        self.browser.get(f"{self.live_server_url}/product")
        self.check_for_product_name_in_products('t-shirt')

    # def test_can_make_a_product_and_retrieve(self):
    #     pass


class Homepage(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'shop/home.html')

from django.db import models
from datetime import datetime

class SubproductManager(models.Manager):
    def get_active_price(self):
        return self.pricing_set.get(is_active=True)


class ProductManager(models.Manager):
    def get_discount(self):
        return self.discount.first(valid_until__gte=datetime.now())
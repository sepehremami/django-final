from django.db import models


class SubproductManager(models.Manager):
    def get_active_price(self):
        return self.pricing_set.get(is_active=True)
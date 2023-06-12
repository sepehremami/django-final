from django.db import models

class OrderInfoManager(models.Manager):
    def retrieve_active_cart(self):
        return self.get(order_status='2')
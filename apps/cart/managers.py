from django.db import models

class OrderInfoManager(models.Manager):
    def retrieve_active_cart(self):
        return self.get(order_status='2')

    def get_total_count(self):
        return self.order_item.aggregate(models.Sum('count'))['count__sum'] 

        
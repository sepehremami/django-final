from django.urls import path
from . import views
urlpatterns = [
    path('<int:product_id>', views.add_to_cart, name='add-to-cart')
]
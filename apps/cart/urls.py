from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"order", views.OrderInfoViewSet, basename="order")
router.register(r"order-item", views.OrderItemViewSet, basename="order-item")
router.register(r'product-discount', views.ProductDiscountViewSet, basename="product-discount")
router.register(r'category-discount', views.CategoryDiscountViewSet, basename="category-discount")
# router.register(r'cart-item', views.AddToCartViewSet, basename='cart-item')

urlpatterns = [
    path('', views.CartTemplateView.as_view(), name='view_cart'),
    path('cart-item/<int:product_id>', views.add_to_cart, name='add-to-cart'),
    path('home', views.add_to_cart, name='home'),
    path("api/", include(router.urls)),
    path('cart-item', views.get_users_cart_items, name='cart-item'), 
    path('api/make-order/', views.final_order, name='order-create')
]

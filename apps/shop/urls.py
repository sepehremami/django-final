from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.ProductListView.as_view(), name="products"),
    path("<int:pk>", view=views.ProductDetailView.as_view(), name="product-detail"),
    path("create", view=views.ProductCreateView.as_view(), name="create-product"),
    path("wishlist", view=views.wishlist, name="wish-list"),
    path('category', view=views.category_dropdown, name='category-dropdown')

]

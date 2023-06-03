from django.urls import path
from . import views
from .api.v1.category import CategoryAPIListView

category_api_urls = [
    path("api/v1/category/", view=CategoryAPIListView.as_view(), name="category-list"),
]

urlpatterns = [
    path("search/", view=views.ProductListView.as_view(), name="products"),
    path("detail/<int:pk>/", view=views.ProductDetailView.as_view(), name="product-detail"),
    path("create/", view=views.ProductCreateView.as_view(), name="create-product"),
    path("category", view=views.CategoryListView.as_view(), name="categories"),
    path("category/<int:pk>", view=views.CategoryDetailView.as_view(), name="category"),
    path("wishlist/", view=views.wishlist, name="wish-list"),
    
] + category_api_urls

from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.ProductView.as_view(), name="product"),
]

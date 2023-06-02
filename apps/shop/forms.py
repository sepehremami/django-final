from django.forms import ModelForm
from .models import Product, Media


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class MediaForm(ModelForm):
    class Meta:
        model = Media
        fields = '__all__'
from django.forms import ModelForm
from main.item import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "price", "description", "size"]
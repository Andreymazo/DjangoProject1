from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'preview', 'price_per_unit', 'category')

        # fields = '__all__'


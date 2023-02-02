from django import forms

from catalog.models import Product, Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        #t = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        model = Subject
        fields = '__all__'#('product_name', 'product_description', 'preview', 'price_per_unit', 'category')
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    # def clean_product_name(self):
    #     t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #     for i in t:
    #
    #     # Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
    #         if Product.product_name == i:
    #             raise ValueError('Nedopustimie slova')




        # fields = '__all__'


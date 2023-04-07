from django import forms
from django.core.exceptions import ValidationError
from django.db.models import CheckConstraint, Q

from catalog.models import Product, Subject, Record


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        # t = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        model = Subject
        # fields = '__all__'
        fields = ('product_name', 'product_description')  # , 'preview', 'price_per_unit', 'category')
        constraints = [
            CheckConstraint(
                check=Q(product_name__gt='казинo'), name='check_product_name',
            ),
        ]

        # def clean(self):
        #
        #     if self.> self.end_date:
        #         # raise error for field
        #         raise ValidationError({'end_date': _('End date cannot be smaller then start date.')})

    def clean_product_name(self):
        t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for i in t:

            if self.product_name == i:
                raise ValidationError({'product_name': 'Nedopustimie slova'})


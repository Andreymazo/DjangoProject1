from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import CASCADE

NULLABLE = {'blank': True, 'null': True}


# class Student(models.Model):
#     # uuid = models.UUIDField(primary_key=True)#Student.objects.get(uuid=1) in shell, vsegda luchshe pk
#     first_name = models.CharField(max_length=250, verbose_name='Имя')
#     last_name = models.CharField(max_length=250, verbose_name='Фамилия')
#
#     avatar = models.ImageField(upload_to='students/', **NULLABLE, verbose_name='Аватар')#Mozhno ne zanosit avatarku
#
#     class Meta:
#         verbose_name = 'студент'
#         verbose_name_plural = 'студенты'
#     def __str__(self):
#         return f'{self.first_name} {self.last_name} '
class Category(models.Model):
    category = models.CharField(max_length=250, verbose_name="Category")
    category_description = models.CharField(max_length=250, verbose_name="Category description")

    def __str__(self):
        return f'{self.category}'


class Product(models.Model):
    STATUS_ACTIV = 'active'
    STATUS_INACTIV = 'inactive'
    STATUSES = (
        (STATUS_ACTIV, 'available'),
        (STATUS_INACTIV, 'no item')
    )
    # created_at = models.CharField(max_length=250, verbose_name='Что-то, что мы щас удалим миграцией')
    # t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    # def clean(self):
    #     t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #
    #     for i in t:
    #         if self.product_name == i:
    #             raise ValidationError('Nedopustimie slova')clean
    product_name = models.CharField(validators=[], max_length=250, verbose_name='Naimenovanie Producta')

    product_description = models.CharField(max_length=250, verbose_name="Product description", **NULLABLE)
    preview = models.ImageField(upload_to='records', **NULLABLE)
    category = models.ForeignKey(Category, related_name="Category", blank=True, max_length=100,
                                 verbose_name="Category description",
                                 on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2, **NULLABLE)
    date_of_creation = models.DateField(auto_now_add=True)
    date_last_change = models.DateField(auto_now=True)
    status = models.CharField(choices=STATUSES, default=STATUS_ACTIV, max_length=20)
    def save(self, *args, **kwargs):
        t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if self.product_name in t:
            raise ValidationError('Nedopustimie slova')
        else:
            super().save(*args, **kwargs)

    # class Meta:
    #     verbose_name = "наименование продукта"
    #     verbose_name_plural = "описание продукта"
    def __str__(self):
        return f"""{self.product_name}{self.preview}  {self.product_description} {self.price_per_unit} {self.status}   """  # {self.id}


class Subject(models.Model):
        product_name_again = models.ForeignKey(Product, on_delete=CASCADE)
        product_content = models.CharField(max_length=150)

        def save(self, *args, **kwargs):
            t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
            if self.product_name_again in t:
                raise ValidationError('Nedopustimie slova')
            else:
                super().save(*args, **kwargs)

    # def clean():
    #     t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #
    #     for i in t:
    #         if Product.product_name == i:
    #             raise ValueError('Nedopustimie slova')



class Record(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = models.CharField(max_length=50, verbose_name="Slug")
    content = models.TextField(max_length=50, null=False, verbose_name='Content')
    image = models.ImageField(upload_to="records", **NULLABLE, default=None)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", **NULLABLE)
    id_public = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_controller = models.IntegerField(default=0, verbose_name="Счетчик просмотров", **NULLABLE)

    # .ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    # class Meta:
    #     verbose_name="Статья"
    #     verbose_name_plural = "Статьи"
    def __str__(self):
        return f'{self.title} {self.content} {self.image} {self.id_public}'

    # def save(self, *args, **kwargs):
    #     t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #     if self.title in t:
    #         raise ValidationError ('Nedopustimie slova')
    #     else:
    #         super().save(*args, **kwargs)
    # class Subject(models.Model):
    #     product_name_again = models.ForeignKey(Product, on_delete=CASCADE)
    #     product_content = models.CharField(max_length=150)
    #
    #     def save(self, *args, **kwargs):
    #         t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #         if self.product_name_again in t:
    #             raise ValidationError('Nedopustimie slova')
    #         else:
    #             super().save(*args, **kwargs)
    # def clean_product_content(self):
    #     t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #     if self.request.method == 'POST':
    #         # form = ProductForm(request.POST, request.FILES)
    #         for i in t:
    #             if self.product_content == i:
    #                 raise ValueError('Nedopustimie slova')
    # if not form.is_valid():
    #
    # else:
    #     return Product.product_name

    # def get_absolut_url(self):
    #     return reverse('catalog: record_detail', kwargs={'slug': self.slug})
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         # Newly created object, so set slug
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

##{self.product_description} {self.date_of_creation}{self.date_last_change}
# class Category(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.name
#
# class Product(models.Model):
#     category = models.ForeignKey(Category, related_name='products')
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ('name',)
#         index_together = (('id', 'slug'),)
#
#     def __str__(self):
#         return self.name

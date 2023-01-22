from django.db import models

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
        return f'{self.category} '
class Product(models.Model):
    # created_at = models.CharField(max_length=250, verbose_name='Что-то, что мы щас удалим миграцией')
    product_name = models.CharField(max_length=250, verbose_name='Naimenovanie Producta')
    product_description = models.CharField(max_length=250, verbose_name="Product description")
    preview = models.ImageField(upload_to='products/', **NULLABLE)#Chto pokazhet ne znau, ##height_field=None, width_field=None, max_length=100
    category = models.ForeignKey(Category, on_delete=models.PROTECT)##Hochu zapretit udalyat category.category poka est products.categry
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    date_of_creation = models.DateField(auto_now_add=True)
    date_last_change = models.DateField(auto_now=True)


    def __str__(self):
        return  f"""{self.id} {self.product_name} {self.category} {self.price_per_unit} """
    from django.db import models

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
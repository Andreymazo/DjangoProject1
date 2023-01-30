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
    preview = models.ImageField(upload_to='image/', **NULLABLE)#Chto pokazhet ne znau, ##height_field=None, width_field=None, max_length=100
    category = models.ForeignKey(Category, related_name="Category", blank=True, max_length=250, verbose_name="Category description", on_delete=models.CASCADE)##Hochu zapretit udalyat category.category poka est products.categry
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    date_of_creation = models.DateField(auto_now_add=True)
    date_last_change = models.DateField(auto_now=True)


    def __str__(self):
        return  f"""{self.product_name}{self.preview}  {self.product_description} {self.price_per_unit}  """#{self.id}

class Record(models.Model):


    title = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = models.CharField(max_length=50, verbose_name="Slug")
    content = models.TextField(max_length=50, null=False, verbose_name='URL')
    image = models.ImageField(upload_to="records", **NULLABLE)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    id_public = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_controller = models.IntegerField(default=0, verbose_name="Счетчик просмотров")
    # .ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    # class Meta:
    #     verbose_name="Статья"
    #     verbose_name_plural = "Статьи"
    def __str__(self):
        return f'{self.title} {self.content} {self.image} {self.id_public}'

    # def get_absolut_url(self):
    #     return reverse('catalog: record_detail', kwargs={'slug': self.slug})
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         # Newly created object, so set slug
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)


    from django.db import models
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
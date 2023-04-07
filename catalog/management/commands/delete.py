from django.core.management import BaseCommand


from catalog.models import Category, Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()

        # ALTER SEQUENCE serial RESTART WITH 105
        Product.objects.all().count()
        Category.objects.all().delete()
        Category.objects.all().count()

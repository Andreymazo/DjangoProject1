
from django.core.management import BaseCommand

# from catalog.models import Student
from catalog.models import Category, Product

class Command(BaseCommand):

    def handle(self, *args, **options):

        jj = [
            {"preview": "static/css/bootstrap.min.css", "product_name": "krab", "category": "moreplavaushie",
             "price_per_unit": "5.5"},
            {"preview": "static/css/bootstrap-reboot.min.css", "product_name": "luk", "category": "trava",
             "price_per_unit": "4.5"},
        ]
        # products_list = []
        for j in jj:
            #     # category_list.append(**i)
            #     products_list.append(Product(product_name=j["product_name"], preview=j["preview"], category=j["category"], price_per_unit=j["price_per_unit"]))
            rec_2 = Product(preview=j["preview"], product_name=j["product_name"], category=j["category"],
                            price_per_unit=j["price_per_unit"])
            rec_2.save()

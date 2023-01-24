
from django.core.management import BaseCommand

# from catalog.models import Student
from catalog.models import Category, Product

class Command(BaseCommand):

    def handle(self, *args, **options):

        jj = [
            {"preview": "media/th.jpeg", "product_name": "lobster", "category": "moreplavaushie",
             "price_per_unit": "5.5"},
            {"preview": "media/apelsin8.jpg", "product_name": "lemon", "category": "fruct",
             "price_per_unit": "4.5"},
            {"preview": "media/th (1).jpeg", "product_name": "onion", "category": "ovosh",
             "price_per_unit": "4.5"},
            {"preview": "media/crab (2).jpeg", "product_name": "crab", "category": "moreplavaushie",
             "price_per_unit": "4.5"},
        ]
        # products_list = []
        for j in jj:
            #     # category_list.append(**i)
            #     products_list.append(Product(product_name=j["product_name"], preview=j["preview"], category=j["category"], price_per_unit=j["price_per_unit"]))
            rec_2 = Product(preview=j["preview"], product_name=j["product_name"], category=j["category"],
                            price_per_unit=j["price_per_unit"])
            rec_2.save()

from django.core.management import BaseCommand

# from catalog.models import Student
from catalog.models import Category, Product

class Command(BaseCommand):

    def handle(self, *args, **options):
        #Product.objects.all().delete()
        # Category.objects.all().delete()
        # print(Category.category)
        # print(type(Category.category))#ImportError: cannot import name 'objects' from 'django.db.models'
        ###Ne mogu 'objects' podcepit, zapisal postrochno, udalit nikak ne mogu. chto ne tak?
        # per = Category.objects.filter(category_contains="s")
        # per._raw_delete(per.db)
        #################Chto-to takoe mozhet srabotalo bi, esli bi ne problema s objects/ Category.category.objects.delete()/bulk_delete???#####

        # Category.category.get().delete()
        ii = [
            {"category": "mebel" , "category_description": "stulya"},
            {"category": "moreplavaushie", "category_description": "ribi"},
            {"category": "trava", "category_description": "v ogorode prorastaemaya"}
        ]
        # category_list = []
        for i in ii:
            # category_list.append(**i)
            # category_list.append(Category(category=i["category"], category_description=i["category_description"]))
            rec_1 = Category(category=i["category"], category_description=i["category_description"])
            rec_1.save()


            # Category.objects.create(category=i["category"], category_description=i["category_description"])
        # Category.objects.bulk_create(category_list)####Ne Rabotaet??????????????????????
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         # print('Hi')
#         students = [
#             {'first_name': 'Oleg', 'last_name': 'Maslov'},
#             {'first_name': 'Smb1', 'last_name': 'Famly1'},
#             {'first_name': 'Smb2', 'last_name': 'Fmly2'},
#             {'first_name': 'Smb3', 'last_name': 'Fmly3'},
#         ]
#         student_list = []
#         for item in students:
#
#             student_list.append(Student(**item))### 3 variant
#             ##1st variant
#             # student = Student(first_name=item['first_name'], last_name=item['last_name'])
#             # student.save()
#             ## 2 variant
#             # Student.objects.create(first_name=item['first_name'], last_name=item['last_name'])
#         Student.objects.bulk_create(student_list)




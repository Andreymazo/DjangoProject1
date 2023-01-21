from django.core.management import BaseCommand

from catalog.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        # print('Hi')
        students = [
            {'first_name': 'Oleg', 'last_name': 'Maslov'},
            {'first_name': 'Smb1', 'last_name': 'Famly1'},
            {'first_name': 'Smb2', 'last_name': 'Fmly2'},
            {'first_name': 'Smb3', 'last_name': 'Fmly3'},
        ]
        student_list = []
        for item in students:

            student_list.append(Student(**item))### 3 variant
            ##1st variant
            # student = Student(first_name=item['first_name'], last_name=item['last_name'])
            # student.save()
            ## 2 variant
            # Student.objects.create(first_name=item['first_name'], last_name=item['last_name'])
        Student.objects.bulk_create(student_list)




from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Student(models.Model):
    # uuid = models.UUIDField(primary_key=True)#Student.objects.get(uuid=1) in shell, vsegda luchshe pk
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')

    avatar = models.ImageField(upload_to='students/', **NULLABLE, verbose_name='Аватар')

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
    def __str__(self):
        return f'{self.first_name} {self.last_name} '

# Generated by Django 4.1.5 on 2023-01-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]

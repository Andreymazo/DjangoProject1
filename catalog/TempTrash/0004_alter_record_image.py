# Generated by Django 4.1.5 on 2023-01-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_record_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='records'),
        ),
    ]

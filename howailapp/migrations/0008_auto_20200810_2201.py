# Generated by Django 3.1 on 2020-08-10 19:01

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howailapp', '0007_divisionproductpattern'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divisionproductpattern',
            name='photopattern',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage('C:\\Users\\Raffy\\Documents\\AlHowailGroup\\static', 'pattern'), upload_to='pattern'),
        ),
    ]

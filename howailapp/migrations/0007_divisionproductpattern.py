# Generated by Django 3.1 on 2020-08-10 12:47

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('howailapp', '0006_divisionproductsizes'),
    ]

    operations = [
        migrations.CreateModel(
            name='DivisionProductPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sizepattern', models.CharField(max_length=200)),
                ('photopattern', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/static/pattern'), upload_to='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('divisionproducttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='howailapp.divisionproducttype')),
            ],
            options={
                'ordering': ['sizepattern'],
            },
        ),
    ]

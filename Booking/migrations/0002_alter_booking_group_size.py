# Generated by Django 3.2.20 on 2023-08-17 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='group_size',
            field=models.PositiveIntegerField(default=100, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(500)]),
        ),
    ]

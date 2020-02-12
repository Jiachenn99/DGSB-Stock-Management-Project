# Generated by Django 3.0.3 on 2020-02-12 08:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_irrigation_tools'),
    ]

    operations = [
        migrations.AlterField(
            model_name='irrigation',
            name='Quantity',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='tools',
            name='Quantity',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

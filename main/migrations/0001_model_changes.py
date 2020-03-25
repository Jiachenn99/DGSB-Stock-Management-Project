# Generated by Django 2.2.7 on 2020-03-21 16:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchasing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pv_no', models.CharField(blank=True, max_length=20)),
                ('invoice_no', models.CharField(blank=True, max_length=20)),
                ('purchasing_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Purchasing',
            },
        ),
        migrations.CreateModel(
            name='Spareparts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spare_parts_name', models.CharField(max_length=30)),
                ('spare_parts_unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('spare_parts_quantity', models.PositiveIntegerField(default=0)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'spare_parts',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'Supplier',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=30)),
                ('vehicle_name', models.CharField(max_length=50)),
                ('vehicle_number_plate', models.CharField(max_length=10)),
                ('vehicle_owner', models.CharField(max_length=30)),
                ('spare_parts_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Spareparts')),
            ],
            options={
                'db_table': 'vehicle',
            },
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'tools',
            },
        ),
        migrations.CreateModel(
            name='Surfacetant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'surfacetant',
            },
        ),
        migrations.CreateModel(
            name='Stationery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'stationery',
            },
        ),
        migrations.AddField(
            model_name='spareparts',
            name='vehicle_assigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Vehicle'),
        ),
        migrations.AddField(
            model_name='purchasing',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Supplier'),
        ),
        migrations.CreateModel(
            name='Pesticide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'pesticide',
            },
        ),
        migrations.CreateModel(
            name='Irrigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'irrigation',
            },
        ),
        migrations.CreateModel(
            name='Herbicide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'herbicide',
            },
        ),
        migrations.CreateModel(
            name='Fungicide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'fungicide',
            },
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'fertilizer',
            },
        ),
        migrations.CreateModel(
            name='Consumables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'consumables',
            },
        ),
    ]
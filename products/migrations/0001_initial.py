# Generated by Django 5.0.7 on 2024-07-30 21:31

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                (
                    'base_price',
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name='Base price',
                    ),
                ),
                (
                    'product',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='tariffs',
                        to='products.product',
                        verbose_name='Product',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Tariff',
                'verbose_name_plural': 'Tariffs',
                'db_table': 'tariffs',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                (
                    'discount',
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(100)
                        ],
                        verbose_name='Percentage of discount',
                    ),
                ),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(verbose_name='End date')),
                (
                    'product',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='promotions',
                        to='products.product',
                        verbose_name='Product',
                    ),
                ),
                (
                    'tariffs',
                    models.ManyToManyField(
                        related_name='promotions',
                        to='products.tariff',
                        verbose_name='Tariffs',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
                'db_table': 'promotions',
            },
        ),
    ]

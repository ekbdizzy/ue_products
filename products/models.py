from django.core.validators import MaxValueValidator
from django.db import models


class Product(models.Model):
    """Model for products."""

    name = models.CharField(max_length=255, verbose_name='Name')

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Tariff(models.Model):
    """Model for tariffs."""

    name = models.CharField(max_length=255, verbose_name='Name')
    base_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Base price'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='tariffs',
        verbose_name='Product',
    )

    class Meta:
        db_table = 'tariffs'
        verbose_name = 'Tariff'
        verbose_name_plural = 'Tariffs'

    def __str__(self):
        return self.name


class Promotion(models.Model):
    """Model for promotions."""

    name = models.CharField(max_length=255, verbose_name='Name')
    discount = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(99)],
        verbose_name='Percentage of discount',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='promotions',
        verbose_name='Product',
    )
    start_date = models.DateField(verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')
    tariffs = models.ManyToManyField(
        Tariff,
        related_name='promotions',
        verbose_name='Tariffs',
    )

    class Meta:
        db_table = 'promotions'
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'

    def __str__(self):
        return self.name

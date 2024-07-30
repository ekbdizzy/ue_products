from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import (
    Subquery,
    ExpressionWrapper,
    Value,
    F,
    OuterRef,
    Prefetch,
)
from django.db.models.functions import Coalesce


class ProductManager(models.QuerySet):
    """Manager for products."""

    def get_all_with_discounted_tariffs(self) -> models.QuerySet:
        """Get products with the biggest discount."""
        queryset = self.prefetch_related(
            Prefetch(
                'tariffs', queryset=Tariff.objects.get_with_biggest_discount()
            )
        )
        return queryset


class Product(models.Model):
    """Model for products."""

    name = models.CharField(max_length=255, verbose_name='Name')

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    objects = ProductManager.as_manager()

    def __str__(self):
        return self.name


class TariffManager(models.QuerySet):
    """Manager for tariffs."""

    @staticmethod
    def get_with_biggest_discount() -> models.QuerySet:
        """Get tariffs with the biggest discount."""

        promotion_subquery = Promotion.objects.filter(
            tariffs=OuterRef('pk')
        ).order_by('-discount')[:1]

        queryset = Tariff.objects.annotate(
            discount=Subquery(
                promotion_subquery.values('discount'),
                output_field=models.IntegerField(),
            ),
            discount_end_date=Subquery(
                promotion_subquery.values('end_date'),
                output_field=models.DateField(),
            ),
            promo_name=Subquery(
                promotion_subquery.values('name'),
                output_field=models.CharField(),
            ),
            price_with_discount=ExpressionWrapper(
                F('base_price')
                - (F('base_price') * Coalesce(F('discount'), Value(0)) / 100),
                output_field=models.DecimalField(
                    max_digits=10, decimal_places=2
                ),
            ),
        )
        return queryset


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

    objects = TariffManager.as_manager()

    def __str__(self):
        return self.name


class Promotion(models.Model):
    """Model for promotions."""

    name = models.CharField(max_length=255, verbose_name='Name')
    discount = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100)],
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

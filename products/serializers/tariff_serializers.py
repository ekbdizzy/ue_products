from rest_framework import serializers
from products.models import Tariff


class TariffSerializer(serializers.ModelSerializer):
    """Serializer for tariff model."""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    base_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    discount = serializers.IntegerField(max_value=100)
    discount_end_date = serializers.DateField(read_only=True)
    price_with_discount = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Tariff
        fields = (
            'id',
            'name',
            'base_price',
            'discount',
            'discount_end_date',
            'price_with_discount',
        )

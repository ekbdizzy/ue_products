from rest_framework import serializers
from products.models import Product
from products.serializers.tariff_serializers import TariffSerializer


class ProductSerializer(serializers.Serializer):
    """Serializer for product model."""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    tariffs = TariffSerializer(many=True, read_only=True, source='tariffs.all')

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'tariffs',
        )

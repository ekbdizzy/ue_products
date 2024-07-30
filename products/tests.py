from django.test import TestCase
from products.models import Product, Promotion, Tariff
from django.urls import reverse
from products.serializers.product_serializers import ProductSerializer


class GetProductsTestCase(TestCase):

    def setUp(self):
        self.product_1 = Product.objects.create(name='Product 1')
        self.product_2 = Product.objects.create(name='Product 2')

        self.tariff_1 = Tariff.objects.create(
            name='Tariff 1', base_price=1000, product=self.product_1
        )
        self.tariff_2 = Tariff.objects.create(
            name='Tariff 2', base_price=2000, product=self.product_1
        )

        self.promo_1 = Promotion.objects.create(
            name='Promo 10',
            product=self.product_1,
            discount=10,
            start_date='2024-07-01',
            end_date='2024-08-01',
        )
        self.promo_2 = Promotion.objects.create(
            name='Promo 20',
            product=self.product_1,
            discount=20,
            start_date='2024-07-01',
            end_date='2024-08-01',
        )
        self.promo_1.tariffs.add(self.tariff_1)
        self.promo_1.tariffs.add(self.tariff_2)

        self.promo_2.tariffs.add(self.tariff_1)

    def test_ProductListView(self):
        """Test ProductListView."""

        response = self.client.get(
            reverse('products:product-list'), format='xml'
        )
        assert response.status_code == 200
        serializer = ProductSerializer(data=response.data, many=True)
        data = serializer.validate(response.data)
        assert data == [
            {
                'id': 1,
                'name': 'Product 1',
                'tariffs': [
                    {
                        'id': 1,
                        'name': 'Tariff 1',
                        'base_price': '1000.00',
                        'discount': 20,
                        'discount_end_date': '2024-08-01',
                        'price_with_discount': '800.00',
                    },
                    {
                        'id': 2,
                        'name': 'Tariff 2',
                        'base_price': '2000.00',
                        'discount': 10,
                        'discount_end_date': '2024-08-01',
                        'price_with_discount': '1800.00',
                    },
                ],
            },
            {'id': 2, 'name': 'Product 2', 'tariffs': []},
        ]

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.services.product_service import ProductService, IProductService
from products.serializers.product_serializers import ProductSerializer


class ProductListView(APIView):
    """View for getting products."""

    serializer_class = ProductSerializer
    product_service: IProductService = ProductService()

    def get(self, request):
        """Get products with the biggest discount in tariff's promos."""

        products = self.product_service.get_products()
        serializer = self.serializer_class(instance=products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

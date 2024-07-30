from abc import ABC, abstractmethod
from django.db.models import QuerySet, Model
from products.models import Product


class IProductService(ABC):
    """Interface for product service."""

    model: Model = None

    @abstractmethod
    def get_products(self):
        """Get products."""
        pass


class ProductService(IProductService):
    """Service for products."""

    model = Product

    def get_products(self) -> QuerySet:
        """Get products."""
        products = self.model.objects.get_all_with_discounted_tariffs()
        return products

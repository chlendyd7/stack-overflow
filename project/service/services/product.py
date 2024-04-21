from django.db import transaction

from service.models.product import Product

    
class ProductService:
    
    @transaction.atomic()
    def creat(
        self,
        name,
        content,
        sale_started_at=None,
        sale_ended_at=None,
        price=None,
        discount=None,
        category_id=None,
    ) -> Product:
        pass



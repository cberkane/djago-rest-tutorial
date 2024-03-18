from rest_framework.viewsets import ReadOnlyModelViewSet

from shop.serializers import ProductSerializer
from shop.models import Product 


class ProductViewset(ReadOnlyModelViewSet):
    
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all()

        category_id = self.request.GET.get('category_id')
        if category_id:
            products = products.filter(category_id=category_id)
        
        inactive = self.request.GET.get('inactive') == 'true'
        if inactive:
            products = products.filter(active=False)
        else:
            products = products.filter(active=True)

        return products
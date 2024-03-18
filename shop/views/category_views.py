from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet

from shop.serializers import CategorySerializer
from shop.serializers import CategoryDetailSerializer
from shop.models import Category 


class CategoryViewset(ReadOnlyModelViewSet):

    def get_queryset(self):
        return Category.objects.filter(active=True)
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoryDetailSerializer
        else:
            return CategorySerializer
        

class AdminCategoryViewset(ModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
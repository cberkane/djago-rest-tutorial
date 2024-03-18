from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from shop.serializers import ArticleSerializer
from shop.models import Article 


class ArticleViewset(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()
    
    @action(detail=True, methods=['GET'])
    def describe(self, request, pk):
        article : Article = self.get_object()
        description = article.describe()

        return Response(data={'description': description})
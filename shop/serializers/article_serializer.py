from rest_framework.serializers import ModelSerializer
from shop.models import Article

class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = ['name', 'price', 'product', 'active']

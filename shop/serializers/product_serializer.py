from rest_framework.serializers import ModelSerializer, SerializerMethodField

from shop.serializers import ArticleSerializer
from shop.models import Product
from shop.models import Article

class ProductSerializer(ModelSerializer):

    articles = SerializerMethodField(method_name='get_articles')

    class Meta:
        model = Product
        fields = ['id', 'name', 'date_created', 'category', 'ecoscore', 'articles']


    def get_articles(self, instance: Article):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data


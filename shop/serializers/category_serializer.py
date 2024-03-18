from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from rest_framework.serializers import ValidationError

from shop.serializers import ProductSerializer
from shop.models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

    def validate_name(self, data):
        ('validate_name')
        if Category.objects.filter(name=data).exists():
            raise ValidationError('Category already exists')
        else:
            return data
        
    def validate(self, data):
        print('validate', data)
        if data['name'] not in data['description']:
            raise ValidationError('Name must be in description')
        else:
            return data


class CategoryDetailSerializer(ModelSerializer):

    products = SerializerMethodField(method_name='get_products')

    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created', 'products']

    def get_products(self, instance):
        queryset = instance.products.all()
        serializer = ProductSerializer(queryset, many=True)
        return serializer.data
    
    
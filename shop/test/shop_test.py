from datetime import date
from rest_framework.test import APITestCase

from shop.models import Category    



class ShopAPITestCase(APITestCase):

    @classmethod
    def setup_data(cls):
        print('*** called ***')

    def format_datetime(self, value: date):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    def create_category(self, name, description, active):
        return Category.objects.create(name=name, description=description, active=active)
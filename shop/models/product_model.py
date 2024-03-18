from django.db import models
from requests import request

    
class Product(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    category = models.ForeignKey('shop.Category', related_name='products', on_delete=models.CASCADE)
    
    @property
    def ecoscore(self):
        response = request('GET', 'https://world.openfoodfacts.org/api/v0/product/3229820787015.json')
        if response.status_code == 200:
            return response.json()['product']['ecoscore_grade']
        
    def __str__(self):
        return self.name
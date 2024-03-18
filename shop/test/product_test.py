from django.urls import reverse_lazy

from shop.test.shop_test import ShopAPITestCase

class TestCategory(ShopAPITestCase):

    def test_list(self):
        url = reverse_lazy('category-list')
        category = self.create_category('fruits', 'les fruits du démon', True)

        response = self.client.get(url)
        expected = [
            {
                'id': category.id,
                'name': category.name, 
                'active': True,
                'date_created': self.format_datetime(category.date_created),
                'products': []
            }
        ]

        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json(), expected)


    def test_detail(self):
        category = self.create_category()
        expected = {
            'id': category.pk, 
            'name': category.name, 
            'active': category.active, 
            'date_created': self.format_datetime(category.date_created),
            'products': []
        }

        url = reverse_lazy('category-detail', kwargs={'pk': '1'})
        response = self.client.get(url)
        self.assertEqual(response.json(), expected)


    # def test_create(self):
    #     response = self.client.post(path=self.get_url(), data={'name': 'Tetative', 'active': True})
    #     self.assertEqual(response.status_code, 405)
    #     self.assertFalse(Category.objects.exists())

    

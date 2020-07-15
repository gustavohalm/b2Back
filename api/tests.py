from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Category, Product


categories_mock = [
    {
        'name': 'Categoria'
    },
    {
        'name': 'Sub Categoria',
        'parent_id': 1
    },
    {
        'name': 'delete category'
    }
]

products_mocks = [
    {
        'name': 'Product 01',
        'description': 'Description',
        'price': 10.63,
        'category_id': 1
    },
    {
        'name': 'Product 02',
        'description': 'Description',
        'price': 10.66,
        'category_id': 2
    },
    {
        'name': 'Product 03',
        'description': 'Description',
        'price': 1000004.66,
        'category_id': 2
    },
    {
        'name': 'Product 04',
        'description': 'Description',
        'price': 1000004.66,
        'category_id': 1
    },
]


def create_mocks():
    for category in categories_mock:
        parent = Category.objects.get(pk=category['parent_id']) if 'parent_id' in category else None
        Category.objects.create(name=category['name'], parent=parent)

    for product in products_mocks:
        category = Category.objects.get(pk=product['category_id'])
        Product.objects.create(name=product['name'], description=product['description'], price=product['price'], category=category)


class CategoryTest(TestCase):
    """
        Test's for Category endpoint
    """

    def setUp(self):
        self.url = '/api/categories/'
        self.client = APIClient()
        create_mocks()

    def test_create(self):
        res = self.client.post(self.url, {'name': 'Categoria Create'}, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_list_with_name(self):
        res = self.client.get(self.url, {'name': 'Categoria'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()[0]['name'], 'Categoria')

    def test_update(self):
        res = self.client.put(self.url+'1/', {'name': 'Categoria 01'}, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()['name'], 'Categoria 01')

    def test_delete(self):
        res = self.client.delete(self.url+'3/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


class ProductTest(TestCase):
    """
          Test's for Category endpoint
    """

    def setUp(self):
        self.url = '/api/products/'
        self.client = APIClient()
        create_mocks()

    def test_create(self):
        new_product = {
            'name': 'Product Create',
            'description': 'desc',
            'category_id': 3,
            'price': 11.99
        }
        res = self.client.post(self.url, new_product, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_list_with_name(self):
        res = self.client.get(self.url, {'name': 'Product 01'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()['results'][0]['name'], 'Product 01')

    def test_update(self):
        update_product = {
            'name': 'Product 01 Change',
            'description': 'description',
            'category_id': 3,
            'price': 8911.99
        }

        res = self.client.put(self.url+'1/', update_product, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()['name'], 'Product 01 Change')

    def test_delete(self):
        res = self.client.delete(self.url+'3/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

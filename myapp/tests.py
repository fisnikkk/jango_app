from django.test import TestCase
from django.urls import reverse
from myapp.models import Product


class ProductListViewTests(TestCase):
    def test_product_list_view_with_no_products(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Products')
        self.assertQuerysetEqual(response.context['products'], [])

    def test_product_list_view_with_products(self):
        Product.objects.create(name='Test Product', description='Test Description', price=9.99)
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Products')
        self.assertQuerysetEqual(response.context['products'], ['<Product: Test Product>'])

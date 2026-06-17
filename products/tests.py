from django.test import TestCase
from .models import Product, Category, Tag
from django.urls import reverse

class ProductListViewTests(TestCase):
    def setUp(self):
        self.coffee = Category.objects.create(name='Coffee Drinks')
        self.bakery = Category.objects.create(name='Bakery')
        self.hot = Tag.objects.create(name='Hot')
        self.iced = Tag.objects.create(name='Iced')
        self.vegan = Tag.objects.create(name='Vegan')
        self.latte = Product.objects.create(name='Latte', description='Coffee with milk', category=self.coffee)
        self.latte.tags.add(self.hot, self.vegan)
        self.muffin = Product.objects.create(name='Muffin', description='Vegan Blueberry muffin', category=self.bakery)
        self.muffin.tags.add(self.vegan)

    def test_page_loads(self):
        # test that the search product page loads successfully
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_search_by_name(self):
        # test searching products by name
        response = self.client.get(reverse('product_list'), {'search': 'Latte'})
        self.assertContains(response, 'Latte')
        self.assertNotContains(response, 'Muffin')

    def test_search_by_description(self):
        # test searching products by description
        response = self.client.get(reverse('product_list'), {'search': 'milk'})
        self.assertContains(response, 'Latte')
        self.assertNotContains(response, 'Muffin')

    def test_filter_by_category(self):
        # test filtering products by category
        response = self.client.get(reverse('product_list'), {'category': self.coffee.id})
        self.assertContains(response, 'Latte')
        self.assertNotContains(response, 'Muffin')

    def test_filter_by_single_tag(self):
        # test filtering products by a single tag
        response = self.client.get(reverse('product_list'), {'tags': self.hot.id})
        self.assertContains(response, 'Latte')
        self.assertNotContains(response, 'Muffin')
    
    def test_filter_by_multiple_tags(self):
        # test filtering products by multiple tags: should return products that have all selected tags
        response = self.client.get(reverse('product_list'), {'tags': [self.hot.id, self.vegan.id]})
        self.assertContains(response, 'Latte')
        self.assertNotContains(response, 'Muffin')

    def test_combined_filters(self):
        # test combining search and filters
        response = self.client.get(reverse('product_list'), {'search': 'Latte', 'category': self.coffee.id, 'tags': self.hot.id})
        self.assertContains(response, 'Latte')
        self.assertNotContains(response, 'Muffin')

    def test_no_results(self):
        # when filters don't match any products, the page should indicate no results found
        response = self.client.get(reverse('product_list'), {'search': 'Espresso', 'category': self.coffee.id, 'tags': self.iced.id})
        self.assertContains(response, 'No items match your search.')

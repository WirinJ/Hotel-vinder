from unicodedata import name
from django.test import TestCase

class ViewsTest(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('127.0.0.1:8000/index')
        self.assertEqual(response.status_code, 404)
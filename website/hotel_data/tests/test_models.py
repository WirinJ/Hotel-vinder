from unicodedata import name
from django.test import TestCase

from hotel_data.models import Hotel, City

class HotelModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        City.objects.create(name='Hotel Test')
        Hotel.objects.create(name='Hotel Test', hotel_tag='TEST001', city_id=1)

    def test_name_max_length(self):
        name = Hotel.objects.get(id=1)
        max_length = name._meta.get_field('name').max_length
        self.assertEqual(max_length, 125)


class CityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        City.objects.create(name='Hotel Test')

    def test_name_max_length(self):
        name = City.objects.get(id=1)
        max_length = name._meta.get_field('name').max_length
        self.assertEqual(max_length, 125)
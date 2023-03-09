from django.test import TestCase
from . models import *
from django.urls import reverse
import json
from django.test import TestCase, Client
from rest_framework import status


# def create_city(name,region):
#     return City.objects.create(name=name,
#     region=region,country="Ethiopia")

# class CityTest(TestCase):
#     def setUp(self):
#         City.objects.create(name="Jimma",region="Oromia",country="Ethio")
#     def test_city_can_exist(self):
#         """ test case for city model to add """
#         try:
#             city = City.objects.get(name="Jimma")
#             self.assertEqual(city.name,"Jimma", 'the city has name')
#         except Exception as e:
#             print("error has occurred",e.message)

# class TryDjangoTesting(TestCase):
#      def test_something(self):
#         # in the try block write all testing and in the except block just tell if there is an error
#         try:
#           pass  
#         except Exception as e:
#             print('thereris an error', {e.message})

# class CinemaIndexView(TestCase):
#     def test



# class IndexViewTestCase(TestCase):

#     def setUp(self):
#         self.client = Client()

#     def test_index_view(self):
#         response = self.client.get('')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         response_data = json.loads(response.content.decode('utf-8'))
#         self.assertIn('YOUR IP ADDRESS', response_data)
#         self.assertIn('YOur COuntry', response_data)
#         self.assertIn('Movies', response_data)
#         self.assertIn('cinema', response_data)
#         self.assertIn('Cast', response_data)
#         self.assertIn('crew', response_data)

class MoviesViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
        def test_its_working(self):
            response = self.client.get('')
            self.assertEqual(response.status_code , status.HTTP_404_NOT_FOUND)

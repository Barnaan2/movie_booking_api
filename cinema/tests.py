from django.test import TestCase
from . models import *
from django.urls import reverse
import json
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APIClient


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
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        # response_data = json.loads(response.content.decode('utf-8'))
        # self.assertIn(None,response.data)


"""
All aviliable methods for testing
"""
# class MyTestCase(TestCase):
#     def test_my_function(self):
#         result = my_function('hello')
#         self.assertEqual(result, 'HELLO')
#         self.assertNotEqual(result, 'hello')
#         self.assertTrue(result.isupper())
#         self.assertIn('L', result)
#         self.assertIsNotNone(result)
#         self.assertRaises(TypeError, my_function, 123)

class CinemaViewIndexTest(TestCase):
    def setUp(self):
        self.client = Client()
    #checking wether or not the the endpoint can be accessed without authorization.
    def test_city(self):
        response = self.client.get('/cinema/cities/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # self.assertIn
    def test_facility(self):
        response = self.client.get('/cinema/facilities/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)













"""
HERE I WILL TEST MODELS 

"""
def create_city(name,region):
    return City.objects.create(name=name,region=region)

def create_facility(name,type):
    return Facility.objects.create(name=name,type=type)




class CinemaModelTestCase(TestCase):
    def setUp(self):
      create_city(name='jimma',region='Oromia')
      create_facility(name='snack for cinemas', type="facility for cinema")

    def test_city_model(self):
        region = City.objects.get(name="jimma").region
        name = City.objects.get(region='Oromia').name
        self.assertEqual(region,'Oromia')
        self.assertEqual(name,'jimma')
    
    def test_facility_model(self):
        facl_type = Facility.objects.get(name="snack for cinemas").type
        self.assertEqual(facl_type,"facility for cinema")



class AddFacilityTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('add-facility')
        print(self.url)
    def test_add_facility(self):
        data = {
            'name': 'Test Facility',
            'type': 'Test Type'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Facility.objects.count(), 1)
        facility = Facility.objects.get()
        self.assertEqual(facility.name, 'Test Facility')
        self.assertEqual(facility.type, 'Test Type')
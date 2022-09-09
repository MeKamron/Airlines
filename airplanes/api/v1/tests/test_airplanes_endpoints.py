from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from airplanes.models import Airplane


class AirplaneTestCase(APITestCase):
    def test_create_airplane(self):
        url = reverse('airplane-list')
        data = {'id': 10, 'num_of_passengers': 300}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 1)
        self.assertEqual(Airplane.objects.get().id, 10)
        self.assertEqual(Airplane.objects.get().num_of_passengers, 300)

    def test_list_airplane(self):
        url = reverse('airplane-list')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 0)

        Airplane.objects.create(id=1, num_of_passengers=100)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

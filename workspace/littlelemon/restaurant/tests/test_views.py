from django.test import TestCase
from ..models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Burger", price=50, inventory=200)
        Menu.objects.create(title="Pizza", price=150, inventory=50)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

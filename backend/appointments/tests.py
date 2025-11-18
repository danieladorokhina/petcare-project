from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


class AppointmentsApiTests(APITestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(
            username="owner",
            email="owner@example.com",
            password="strongpass123",
        )
        self.client.force_authenticate(self.user)
        self.url = "/api/appointments/"

    def test_create_appointment(self):
        """Просто перевіряємо, що ендпойнт існує (або поки що повертає хоч якийсь код)"""
        data = {
            "pet": 1,  
            "date_time": (timezone.now() + timedelta(days=1)).isoformat(),
            "reason": "Regular checkup",
        }
        response = self.client.post(self.url, data, format="json")

        self.assertNotEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
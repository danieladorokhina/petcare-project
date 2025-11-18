from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class RegistrationTests(APITestCase):
    def setUp(self):
        self.url = "/api/accounts/register/"

    def test_register_user_success(self):
        """Успішна реєстрація користувача"""
        data = {
            "email": "admin@example.com",
            "password": "adequate_pass12",
            "password2": "adequate_pass12",
        }
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="admin@example.com").exists())

    def test_register_user_password_mismatch(self):
        """Валідація: паролі не співпадають"""
        data = {
            "email": "user2@example.com",
            "password": "adequate_pass12",
            "password2": "another_pass13",
        }
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", str(response.data).lower())
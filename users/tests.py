from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

LIST_USER_URL = reverse('user-list')
TOKEN_URL = reverse('api_token_auth')


def create_user(**data):
    return get_user_model().objects.create_user(**data)


class CreateUserApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user(self):
        """Creating new user test"""
        data = {
            "username": "testUser",
            "is_active": "true",
            "password": "password123"
        }

        result = self.client.post(LIST_USER_URL, data)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**result.data)
        self.assertTrue(user.check_password(data['password']))
        self.assertNotIn('password', result.data)

    def test_create_existing_user(self):
        """Creating already existing user"""

        data = {
            "username": "testUser2",
            "is_active": "true",
            "password": "password123"
        }

        # to avoid using serializer in that test
        data2 = {
            "username": "testUser2",
            "is_active": True,
            "password": "password123"
        }
        create_user(**data2)
        result = self.client.post(LIST_USER_URL, data)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token(self):
        """Creating token for existing user test"""
        data = {
            "username": "testUser3",
            "is_active": True,
            "password": "password123"
        }
        create_user(**data)
        data.pop('is_active')
        result = self.client.post(TOKEN_URL, data)
        self.assertIn('token', result.data)
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_create_token_wrong_credentials(self):
        """Creating token for existing user with wrong credentials test"""
        data = {
            "username": "testUser4",
            "is_active": True,
            "password": "password123"
        }
        create_user(**data)
        result = self.client.post(TOKEN_URL, {"username": "testUser4", "password": "shitpassword"})
        self.assertNotIn('token', result.data)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_toke_no_user(self):
        """Creating token for not existing user test"""
        data = {
            "username": "testUser5",
            "password": "password123"
        }
        result = self.client.post(TOKEN_URL, data)
        self.assertNotIn('token', result.data)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

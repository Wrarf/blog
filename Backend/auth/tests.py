from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

from auth.serializers import UserSerializer


class UsersTestCase(APITestCase):
    """Test suite for the API views related to users."""
    @classmethod
    def setUpTestData(cls):
        """Create a new user."""
        user = {
            'username': 'user1',
            'email': 'user1@email.com',
            'password': 'P455w0Rd'
        }

        client = APIClient()
        client.post('/users/', user, format='json')

    def test_create_user(self):
        """Ensure we can create a new user."""
        self.assertEqual(get_user_model().objects.count(), 1)

    def test_get_user(self):
        """Ensure we can read user's informations with the API."""
        response = self.client.get('/users/1/', format='json')
        user = get_user_model().objects.first()

        self.assertEqual(response.data['username'], user.username)

    def test_password_hashing(self):
        """Ensure that the password is hashed."""
        user = get_user_model().objects.first()

        self.assertNotEqual(user.password, 'P455w0Rd')
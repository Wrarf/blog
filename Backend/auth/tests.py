from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse

from auth.serializers import UserSerializer


class UsersTestCase(APITestCase):
    """Test suite for the API views related to users."""
    def test_create_user(self):
        """Ensure we can create a new user."""
        user = {
        'username': 'user1',
        'email': 'user1@email.com',
        }
        response = self.client.post('/users/', user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'user1')

    def test_get_user(self):
        """Ensure we can read user's informations with the API."""
        user = User.objects.create(username='user1', email='user1@email.com')
        response = self.client.get('/users/1/', format='json')
        self.assertEqual(response.data['username'], user.username)
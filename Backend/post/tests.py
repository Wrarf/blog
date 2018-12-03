from rest_framework.test import APITestCase, APIClient
from post.models import Post, Comment
from django.contrib.auth import get_user_model
import os


class PostTestCase(APITestCase):
	'''Test suite for the API views related to posts.'''
	@classmethod
	def setUpTestData(cls):
		'''Create a new post'''
		admin = get_user_model().objects.create(
			username='admin', password='4dm1n15tr4t0r', email='admin@admin.com')
		admin.is_staff = True
		admin.save()

		client = APIClient()
		client.force_authenticate(user=admin)
		dirname = os.path.dirname(__file__)
		with open(os.path.join(dirname, 'test_utils/test.png'), 'rb') as img:
			post = {
				'title': 'Article 1',
				'img': img,
				'text': 'Post post postpost postpostpost post PoSt pOst'
			}
			client.post('/posts/', post, format='multipart')

	def test_create_post(self):
		'''Ensure we can create a new post.'''
		self.assertEqual(Post.objects.count(), 1)

	def test_get_post(self):
		'''Ensure we can get post informations from API.'''
		response = self.client.get('/posts/1/', format='json')
		post = Post.objects.first()

		self.assertEqual(response.data['title'], post.title)

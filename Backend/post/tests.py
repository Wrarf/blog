from rest_framework.test import APITestCase, APIClient
from post.models import Post, Comment
import os


class PostTestCase(APITestCase):
	'''Test suite for the API views related to posts.'''
	@classmethod
	def setUpTestData(cls):
		'''Create a new post'''
		client = APIClient()
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

	#def test_post_comments(self):

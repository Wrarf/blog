from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Post(models.Model):
	title = models.CharField()
	img = models.ImageField()
	text = models.TextField()
	pub_date = models.DateField(auto_now_add=True)

	def __str__(self):
   		return self.title


class Comment(models.Model):
	text = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	reply_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
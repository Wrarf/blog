from post.models import Post, Comment
from post.serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets


class PostsViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('pub_date')
	serializer_class = PostSerializer


class CommentsViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.filter(reply_to__isnull=True).order_by('pub_date')
	serializer_class = CommentSerializer
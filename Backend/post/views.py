from post.models import Post, Comment
from post.serializers import PostSerializer, CommentSerializer, PostPreviewsSerializer
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, BasePermission


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class PostsViewSet(viewsets.ModelViewSet, APIView):
	queryset = Post.objects.all().order_by('pub_date')
	serializer_class = PostSerializer
	permission_classes = (IsAdminUser|ReadOnly,)

	def get(self, request, format=None):
		content = {
			'status': 'request was permitted'
		}
		return Response(content)


class CommentsViewSet(viewsets.ModelViewSet, APIView):
	queryset = Comment.objects.filter(reply_to__isnull=True).order_by('pub_date')
	serializer_class = CommentSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def get(self, request, format=None):
		content = {
			'status': 'request was permitted'
		}
		return Response(content)


class PostPreviewsViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('pub_date')
	serializer_class = PostPreviewsSerializer
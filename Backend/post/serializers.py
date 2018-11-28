from post.models import Post, Comment
from rest_framework import serializers
from django.contrib.auth import get_user_model


class ReplySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=get_user_model().objects.all())

    class Meta:
        model = Comment
        fields = ('text', 'pub_date', 'user')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=get_user_model().objects.all())
    post = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Post.objects.all())
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'text', 'pub_date', 'user', 'post', 'replies')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    #comments = CommentSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField(method_name='get_original_comments')

    class Meta:
        model = Post
        fields = ('url', 'title', 'img', 'text', 'pub_date', 'comments')

    def get_original_comments(self, obj):
        '''Gets original comments (NOT replies).'''
        return CommentSerializer(
            obj.comments.filter(reply_to__isnull=True), many=True, read_only=True).data

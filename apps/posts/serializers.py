from rest_framework import serializers
from .models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'image', 'description', 'created_at', 'likes_count', 'comments_count')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created_at')


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'post', 'user', 'created_at')

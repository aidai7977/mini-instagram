from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import User, Follow

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'avatar')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user


class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(read_only=True)
    following = serializers.StringRelatedField()

    class Meta:
        model = Follow
        fields = ('id', 'follower', 'following', 'created_at')

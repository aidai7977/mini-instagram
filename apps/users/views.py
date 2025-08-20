from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User, Follow
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]  # JWT аутентификация
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # просмотр для всех, редактирование только для авторизованных
    lookup_field = 'username'

    # Подписаться на пользователя
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def follow(self, request, username=None):
        target_user = self.get_object()
        if target_user == request.user:
            return Response({'detail': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        follow, created = Follow.objects.get_or_create(follower=request.user, following=target_user)
        if created:
            return Response({'detail': f'You are now following {target_user.username}'}, status=status.HTTP_201_CREATED)
        return Response({'detail': f'You already follow {target_user.username}'}, status=status.HTTP_200_OK)

    # Отписаться от пользователя
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unfollow(self, request, username=None):
        target_user = self.get_object()
        follow = Follow.objects.filter(follower=request.user, following=target_user)
        if follow.exists():
            follow.delete()
            return Response({'detail': f'You unfollowed {target_user.username}'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)

    # Список подписчиков
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def followers(self, request, username=None):
        user = self.get_object()
        followers = User.objects.filter(following__following=user)
        serializer = UserSerializer(followers, many=True)
        return Response(serializer.data)

    # Список подписок
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def following(self, request, username=None):
        user = self.get_object()
        following = User.objects.filter(followers__follower=user)
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)

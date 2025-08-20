from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    # Комментарии к посту
    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = Comment.objects.filter(post=post).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def add_comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Лайк / Анлайк
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if created:
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        try:
            like = Like.objects.get(post=post, user=request.user)
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)

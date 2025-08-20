from django.contrib import admin
from .models import Post, Comment, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at')
    search_fields = ('author__username', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_at')
    search_fields = ('author__username', 'text')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('created_at',)


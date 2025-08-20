from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Follow

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('id',)
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('bio', 'avatar')}),
    )

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'created_at')
    search_fields = ('follower__username', 'following__username')


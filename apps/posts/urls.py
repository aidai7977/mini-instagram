from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]

'''
Как это работает
DefaultRouter автоматически создаёт стандартные CRUD URL для постов:

Метод	URL	Действие
GET	/api/posts/	list (список постов)
POST	/api/posts/	create (создать пост)
GET	/api/posts/{pk}/	retrieve (подробности поста)
PUT/PATCH	/api/posts/{pk}/	update (редактировать пост)
DELETE	/api/posts/{pk}/	destroy (удалить пост)

@action методы тоже автоматически подхватываются:

Метод	URL	Действие
GET	/api/posts/{pk}/comments/	comments (список комментариев)
POST	/api/posts/{pk}/add_comment/	add_comment
POST	/api/posts/{pk}/like/	like
POST	/api/posts/{pk}/unlike/	unlike

В core/urls.py (основной urls.py проекта) подключаем:

python
Копировать
Редактировать
path('api/posts/', include('posts.urls')),
После этого все эндпоинты PostViewSet будут доступны по /api/posts/.
'''
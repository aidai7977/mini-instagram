from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]

'''
 Как это работает
DefaultRouter создаёт стандартные CRUD URL для пользователей:

Метод	URL	Действие
GET	/api/users/	list (список всех пользователей)
POST	/api/users/	create (регистрация)
GET	/api/users/{username}/	retrieve (информация о пользователе)
PUT/PATCH	/api/users/{username}/	update
DELETE	/api/users/{username}/	destroy

@action методы тоже автоматически подхватываются:

Метод	URL	Действие
POST	/api/users/{username}/follow/	follow
POST	/api/users/{username}/unfollow/	unfollow
GET	/api/users/{username}/followers/	список подписчиков
GET	/api/users/{username}/following/	список тех, на кого подписан
'''

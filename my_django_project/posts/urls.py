from django.urls import path
# from rest_framework.routers import DefaultRouter
from posts.Api.views import PostList, PostRetrieve, PostCreate, PostUpdate, PostDestroy
# from games.Api.views import GameViewSet


# router = DefaultRouter
# router.register(r'games', GameViewSet)


urlpatterns = [
    path('v1/posts/', PostList.as_view(), name='post-list'),
    path('v1/posts/<int:pk>/', PostRetrieve.as_view(), name='post-detail'),
    path('v1/posts/create/', PostCreate.as_view(), name='post-create'),
    path('v1/posts/<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('v1/posts/<int:pk>/delete/', PostDestroy.as_view(), name='post-destroy'),
] 
# + router.urls
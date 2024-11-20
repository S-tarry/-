from django.urls import path
# from rest_framework.routers import DefaultRouter
from users.Api.views import UserList, UserRetrieve, UserCreate, UserUpdate, UserDestroy
# from games.Api.views import GameViewSet


# router = DefaultRouter
# router.register(r'games', GameViewSet)


urlpatterns = [
    path('v1/users/', UserList.as_view(), name='user-list'),
    path('v1/users/<int:pk>/', UserRetrieve.as_view(), name='user-detail'),
    path('v1/users/create/', UserCreate.as_view(), name='user-create'),
    path('v1/users/<int:pk>/update/', UserUpdate.as_view(), name='user-update'),
    path('v1/users/<int:pk>/delete/', UserDestroy.as_view(), name='user-destroy'),
] 
# + router.urls
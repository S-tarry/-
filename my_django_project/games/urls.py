from django.urls import path
# from rest_framework.routers import DefaultRouter
from games.Api.views import GameList, GameRetrieve, GameCreate, GameUpdate, GameDestroy
# from games.Api.views import GameViewSet


# router = DefaultRouter
# router.register(r'games', GameViewSet)


urlpatterns = [
    path('v1/games/', GameList.as_view(), name='game-list'),
    path('v1/games/<int:pk>/', GameRetrieve.as_view(), name='game-detail'),
    path('v1/games/create/', GameCreate.as_view(), name='game-create'),
    path('v1/games/<int:pk>/update/', GameUpdate.as_view(), name='game-update'),
    path('v1/games/<int:pk>/delete/', GameDestroy.as_view(), name='game-destroy'),
] 
# + router.urls
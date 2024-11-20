from rest_framework import viewsets, generics
from games.models.game import Game
from games.serializer.games import GameSerializer
from drf_spectacular.utils import extend_schema


# використання viewset
# class GameViewSet(viewsets.ModelViewSet):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer

#     # отримання списку всіх ігор
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
    
#     # отримання деталей про конкретну гру
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
    
#     # створення нового об'єкту(гри)
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     # оновлення даних про гру  
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     # видалення гри
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


    
@extend_schema(summary="отримання списку всіх ігор")
class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    

@extend_schema(summary="отримання деталей про конкретну гру", description='виводить всі дані про конкретний продукт')
class GameRetrieve(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


@extend_schema(summary="створення нового об'єкту(гри)")
class GameCreate(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


@extend_schema(summary="оновлення даних про гру")
class GameUpdate(generics.UpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    

@extend_schema(summary="видалення гри", description='видаляє гру зі списку')
class GameDestroy(generics.DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
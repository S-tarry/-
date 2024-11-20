from rest_framework import viewsets, generics
from users.models.user import CustomUser
from users.serializer.users import CustomUserSerializer
from rest_framework.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema


# використання viewset
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

#     # отримання списку всіх користувачів
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
    
#     # отримання деталей про конкретного користувача
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
    
#     # створення нового користувача
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     # оновлення даних про користувача  
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     # видалення користувача
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)



@extend_schema(summary="отримання списку всіх користувачів")
class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


@extend_schema(summary="отримання деталей про конкретного користувача")
class UserRetrieve(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


@extend_schema(summary="створення нового користувача", description='додає нового користувача')
class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


@extend_schema(summary="оновлення даних про користувача")
class UserUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
    

@extend_schema(summary="видалення користувача", description='видаляє користувача з бд')
class UserDestroy(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
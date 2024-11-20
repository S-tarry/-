from rest_framework import viewsets, generics
from posts.models.post import Post
from posts.serializer.posts import PostSerializer
from drf_spectacular.utils import extend_schema


# використання viewset
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     # отримання списку всіх постів
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
    
#     # отримання деталей про конкретний пост
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
    
#     # створення нового посту
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     # оновлення даних про пост  
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     # видалення посту
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


    
@extend_schema(summary="отримання списку всіх постів")
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

@extend_schema(summary="отримання деталей про конкретний пост")
class PostRetrieve(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@extend_schema(summary="створення нового посту")
class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@extend_schema(summary="оновлення даних про пост")
class PostUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

@extend_schema(summary="видалення посту")
class PostDestroy(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
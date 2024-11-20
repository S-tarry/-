from rest_framework import viewsets, generics
from orders.models.order import Order
from orders.serializer.orders import OrderSerializer
from drf_spectacular.utils import extend_schema


# використання viewset
# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     # отримання списку всіх замовлень
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
    
#     # отримання деталей про конкретне замовлення
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
    
#     # створення нового замовлення
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     # оновлення даних про замовлення  
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     # видалення замовлення
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


    
@extend_schema(summary="отримання списку всіх замовлень", description='виводить всі замовлення')
class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

@extend_schema(summary="отримання деталей про конкретне замовлення")
class OrderRetrieve(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@extend_schema(summary="створення нового замовлення", description='створює нове замовлення')
class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

  
@extend_schema(summary="оновлення даних про замовлення")
class OrderUpdate(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

@extend_schema(summary="видалення замовлення")
class OrderDestroy(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
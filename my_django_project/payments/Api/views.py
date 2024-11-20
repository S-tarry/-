from rest_framework import viewsets, generics
from payments.models.payment import Payment
from payments.serializer.payments import PaymentSerializer
from drf_spectacular.utils import extend_schema

# використання viewset
# class PaymentViewSet(viewsets.ModelViewSet):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer

#     # отримання списку всіх оплат
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
    
#     # отримання деталей про конкретну оплат
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
    
#     # створення нової оплати
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     # оновлення даних про оплату  
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     # видалення оплати
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


    

@extend_schema(summary="отримання списку всіх оплат")
class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    

@extend_schema(summary="отримання деталей про конкретну оплат")
class PaymentRetrieve(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


@extend_schema(summary="створення нової оплати", description='створює нову оплату')
class PaymentCreate(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


@extend_schema(summary="оновлення даних про оплату")
class PaymentUpdate(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    

@extend_schema(summary="видалення оплати")
class PaymentDestroy(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

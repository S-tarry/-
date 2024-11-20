from django.urls import path
# from rest_framework.routers import DefaultRouter
from orders.Api.views import OrderList, OrderRetrieve, OrderCreate, OrderUpdate, OrderDestroy
# from orders.Api.views import OrderViewSet


# router = DefaultRouter
# router.register(r'games', GameViewSet)


urlpatterns = [
    path('v1/orders/', OrderList.as_view(), name='order-list'),
    path('v1/orders/<int:pk>/', OrderRetrieve.as_view(), name='order-detail'),
    path('v1/orders/create/', OrderCreate.as_view(), name='order-create'),
    path('v1/orders/<int:pk>/update/', OrderUpdate.as_view(), name='order-update'),
    path('v1/orders/<int:pk>/delete/', OrderDestroy.as_view(), name='order-destroy'),
] 
# + router.urls
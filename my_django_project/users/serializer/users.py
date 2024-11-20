from rest_framework import serializers
from users.models.user import CustomUser
from posts.serializer.posts import PostSerializer
from orders.serializer.orders import OrderSerializer



class CustomUserSerializer(serializers.ModelSerializer):
    post = PostSerializer() 
    order = OrderSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email' ,'active', 'post', 'order']
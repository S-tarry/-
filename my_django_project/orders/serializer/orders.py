from rest_framework import serializers
from orders.models.order import Order
from payments.serializer.payments import PaymentSerializer
from games.serializer.games import GameSerializer



class OrderSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer()
    game = GameSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user_id', 'game_id', 'total_price', 'payment', 'game']
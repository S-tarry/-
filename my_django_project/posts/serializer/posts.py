from rest_framework import serializers
from posts.models.post import Post
from games.serializer.games import GameSerializer



class PostSerializer(serializers.ModelSerializer):
    game = GameSerializer()

    class Meta:
        model = Post
        fields = ['id', 'user_id', 'game_id', 'text', 'data_created', 'game']
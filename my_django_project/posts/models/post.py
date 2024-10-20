from django.db import models
from users.models.user import User
from games.models.game import Game


class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.TextField()
    data_created = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.text
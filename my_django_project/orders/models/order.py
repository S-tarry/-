from django.db import models
from users.models.user import User
from games.models.game import Game


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits = 4, decimal_places = 2)
    

    def __str__(self):
        return self.total_price
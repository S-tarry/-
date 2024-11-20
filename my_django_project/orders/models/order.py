from django.db import models
from users.models.user import CustomUser
from games.models.game import Game


class Order(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    game_id = models.OneToOneField(Game, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits = 6, decimal_places = 2)

    def __str__(self):
        return self.total_price
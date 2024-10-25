from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser добавлення полів до встроєного django user
class CustomUser(AbstractUser):
    active = models.BooleanField(default = False)


    def __str__(self):
        return self.username
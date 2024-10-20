from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    developer = models.CharField(max_length=100)


    def __str__(self):
        return self.name
from django.db import models
from orders.models.order import Order

class Payment(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    # order_id = models.ForeignKey(Order, on_delete = models.CASCADE)
    payment_data = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.payment_data
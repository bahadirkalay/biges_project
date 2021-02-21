from django.db import models
from django.contrib.auth.models import User
from product.models import GameModel

# Create your models here.

class ShopCardModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.OneToOneField(GameModel, on_delete=models.SET_NULL , null=True)
    quantity = models.IntegerField()

    @property
    def amount (self):
        return (self.quantity * self.product.price)
    
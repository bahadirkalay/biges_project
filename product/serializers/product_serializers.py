
from rest_framework import serializers
from product.models import GameModel


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields = [
            'name',
            'year',
            'category'

        ]

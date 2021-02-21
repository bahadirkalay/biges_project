from rest_framework import serializers
from order.models import ShopCardModel


class ShopCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCardModel
        fields = [
            'user',
            'product',
            'quantity',

        ]
        depth = 0

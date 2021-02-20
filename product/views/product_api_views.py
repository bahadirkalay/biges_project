from django.shortcuts import render
from rest_framework.generics import ListAPIView
from product.models import GameModel
from product.serializers import ProductSerializers

# Create your views here.

class ProductListApiView(ListAPIView):
    queryset = GameModel.objects.all()
    serializer_class = ProductSerializers

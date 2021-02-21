from django.shortcuts import render
from rest_framework.generics import ListAPIView , CreateAPIView
from product.models import GameModel
from product.serializers import ProductSerializers ,ProductUpdateCreateSerializers

# Create your views here.

class ProductListApiView(ListAPIView):
    queryset = GameModel.objects.all()
    serializer_class = ProductSerializers


class ProductCreatedView(CreateAPIView):
    queryset = GameModel.objects.all()
    serializer_class = ProductUpdateCreateSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
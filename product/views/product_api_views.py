from django.shortcuts import render
from rest_framework.generics import ListAPIView , CreateAPIView
from rest_framework.filters import SearchFilter
from product.models import GameModel
from product.serializers import ProductSerializers ,ProductUpdateCreateSerializers
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ProductListApiView(ListAPIView):
    queryset = GameModel.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'name']

    


class ProductCreatedView(CreateAPIView):
    queryset = GameModel.objects.all()
    serializer_class = ProductUpdateCreateSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
from rest_framework.generics import ListCreateAPIView
from order.models import ShopCardModel
from order.serializers import ShopCardSerializer
from rest_framework.permissions import IsAuthenticated

class ShopCardCreateAPIView (ListCreateAPIView):
    queryset = ShopCardModel.objects.all()
    serializer_class = ShopCardSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return ShopCardModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

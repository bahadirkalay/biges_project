
from django.urls import path, include
from order.views import ShopCardCreateAPIView

urlpatterns = [
    path ('shopcard', ShopCardCreateAPIView().as_view(), name='shopcard'),
    #path ('create', ProductCreatedView().as_view(), name='create')
]

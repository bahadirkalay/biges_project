
from django.urls import path, include
from product.views import ProductListApiView

urlpatterns = [
    path ('list', ProductListApiView().as_view(), name='list')
]

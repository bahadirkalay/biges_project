
from django.urls import path, include
from product.views import ProductListApiView, ProductCreatedView

urlpatterns = [
    path ('list', ProductListApiView().as_view(), name='list'),
    path ('create', ProductCreatedView().as_view(), name='create')
]

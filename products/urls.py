from django.urls import path
from .views import ProductListCreateAPI

urlpatterns = [
    path('products/',ProductListCreateAPI.as_view(), name='product-list-create')
]


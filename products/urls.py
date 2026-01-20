from django.urls import path
from .views import ProductListCreateAPI , StockInAPI,StockOutAPI


urlpatterns = [
    path('products/',ProductListCreateAPI.as_view(), name='product-list-create'),
    path('stock-in/<int:product_id>/',StockInAPI.as_view(),name='stock-in'),
    path('stock-out/<int:product_id>/',StockOutAPI.as_view(),name='stock-out')
]


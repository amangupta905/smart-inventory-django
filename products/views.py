from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .searializers import productSearializers

class ProductListCreateAPI(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = productSearializers



# Create your views here.

from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .searializers import productSearializers

class ProductListCreateAPI(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = productSearializers


class StockInAPI(APIView):
    def post(self, request, product_id):
        print("REQUEST DATA:", request.data)
        quantity = request.data.get('quantity')
        print(quantity)

        if not quantity or int(quantity) <= 0:
            return Response(
                {"error": "Quantity must be greater than zero"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        product.stock += int(quantity)
        product.save()

        return Response({
            "message": "Stock added successfully",
            "product": product.name,
            "current_stock": product.stock
        }, status=status.HTTP_200_OK)

class StockOutAPI(APIView):
    def post(self, request, product_id):
        quantity = request.data.get('quantity')

        if not quantity or int(quantity) <= 0:
            return Response(
                {"error": "Quantity must be greater than zero"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if product.stock < int(quantity):
            return Response(
                {"error": "Not enough stock available"},
                status=status.HTTP_400_BAD_REQUEST
            )

        product.stock -= int(quantity)
        product.save()

        return Response({
            "message": "Stock removed successfully",
            "product": product.name,
            "current_stock": product.stock,
            "low_stock": product.is_low_stock()
        }, status=status.HTTP_200_OK)



# Create your views here.

from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
       return str(self.name) or ""

class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    low_stock_threshold = models.PositiveIntegerField(default=5)

    def is_low_stock(self):
        return self.stock <= self.low_stock_threshold

    def __str__(self):
        return str(self.name) or ""
# Create your models here.

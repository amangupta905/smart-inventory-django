from rest_framework import serializers
from products.models import Category


class productSearializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

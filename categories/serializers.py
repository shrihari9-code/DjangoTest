from rest_framework import serializers
from products.serializers import ProductListSerializer
from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):
    count_products = serializers.IntegerField(read_only=True)
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

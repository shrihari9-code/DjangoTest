from rest_framework import serializers
from products.models import Product, Sku

class ProductListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing products.
    """

    class Meta:
        model = Product
        fields = ["id", "name", "price"]

class SkuSerializer(serializers.ModelSerializer):
    markup_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Sku
        fields = '__all__'

    def get_markup_percentage(self, obj):
        return obj.markup_percentage
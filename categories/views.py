from rest_framework import permissions
from rest_framework.generics import ListAPIView
from categories.models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

@permission_classes([AllowAny])
class CategoryWithProductsListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


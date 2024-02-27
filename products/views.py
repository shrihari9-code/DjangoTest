from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
)
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Product, Sku
from .serializers import ProductListSerializer, SkuSerializer

@api_view(["GET"])
@permission_classes([AllowAny])
def products_list(request):
    """
    List of all products.
    """
    is_refrigerated_param = request.query_params.get('is_refrigerated', '')
    if is_refrigerated_param.lower() == 'true':
        products = Product.objects.filter(is_refrigerated=True)
    elif is_refrigerated_param.lower() == 'false':
        products = Product.objects.filter(is_refrigerated=False)
    else:
        products = Product.objects.all()

    serializer = ProductListSerializer(products, many=True)
    return Response({"products": serializer.data}, status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_sku(request):
    if request.method == 'POST':
        data = request.data.copy()
        data['status'] = 0  # Set status to default (Pending for approval)
        serializer = SkuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductListSerializer(product)
        return Response(serializer.data, status=HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=HTTP_404_NOT_FOUND)
    
@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def edit_sku_status(request, sku_id):
    try:
        sku = Sku.objects.get(id=sku_id)
        new_status = request.data.get('status')
        if new_status is not None:
            sku.status = new_status
            sku.save()
            serializer = SkuSerializer(sku)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response({'error': 'Status field is required'}, status=HTTP_400_BAD_REQUEST)
    except Sku.DoesNotExist:
        return Response({'error': 'Sku not found'}, status=HTTP_404_NOT_FOUND)
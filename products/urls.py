from django.urls import path

from .views import create_sku, products_list,product_details, edit_sku_status

urlpatterns = [
    path("", products_list, name="products-list"),
     path('api/create_sku/', create_sku, name='create_sku'),
    path('api/product_details/<int:product_id>/', product_details, name='product_details'),
    path('api/edit_sku_status/<int:sku_id>/', edit_sku_status, name='edit_sku_status')
]

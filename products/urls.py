from django.urls import path

from .views import create_sku, products_list,product_details, edit_sku_status,active_categories_with_sku_count,skus_with_category

urlpatterns = [
    path("", products_list, name="products-list"),
    path('api/create_sku/', create_sku, name='create_sku'),
    path('api/product_details/<int:product_id>/', product_details, name='product_details'),
    path('api/edit_sku_status/<int:sku_id>/', edit_sku_status, name='edit_sku_status'),
    path('api/active_categories_with_sku_count/', active_categories_with_sku_count, name='active_categories_with_sku_count'),
    path('api/skus_with_category/', skus_with_category, name='skus_with_category'),
]

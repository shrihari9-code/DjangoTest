from django.contrib import admin
from django.urls import include, path
from categories.views import CategoryWithProductsListAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
    path('categories/',include("categories.urls")), 
]

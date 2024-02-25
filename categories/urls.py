from django.urls import path
from categories.views import CategoryWithProductsListAPIView


urlpatterns = [
    path("", CategoryWithProductsListAPIView.as_view(), name="categories-list"),
]

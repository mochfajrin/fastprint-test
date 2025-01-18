from django.urls import path
from app.views import category, status, product

urlpatterns = [
    path("", product.index, name="product")
]

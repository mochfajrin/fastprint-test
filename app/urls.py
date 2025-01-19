from django.urls import path
from app.views import category, status, product

urlpatterns = [
    path("", product.index, name="home"),
    path("products", product.index, name="products"),
    path("products/create", product.create),
    path("products/edit/<id_produk>", product.update),
    path("products/delete/<id_produk>", product.create),
    path("categories", category.index, name="categories"),
    path("api/fastprint", product.fetch_products)
]

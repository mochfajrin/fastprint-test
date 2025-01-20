from django.urls import path
from app.views import category, status, product

urlpatterns = [
    path("", product.index, name="home"),
    path("products", product.index, name="products"),
    path("products/create", product.create),
    path("products/edit/<id_produk>", product.update),
    path("products/delete/<id_produk>", product.delete),
    path("categories", category.index, name="categories"),
    path("categories/create", category.create),
    path("categories/edit/<id_kategori>", category.update),
    path("categories/delete/<id_kategori>", category.delete),
    path("status", status.index, name="status"),
    path("status/create", status.create),
    path("status/edit/<id_status>", status.update),
    path("status/delete/<id_status>", status.delete),
    path("api/fastprint", product.fetch_products)
]

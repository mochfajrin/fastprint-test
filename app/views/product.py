from django.shortcuts import render, redirect, get_object_or_404
from django.core import paginator
from app.api import fastprint


def index(request):
    data = fastprint.getFastPrintProducts()
    unique_categories = set(product["kategori"] for product in data)
    unique_status = set(product["status"] for product in data)

    print(unique_categories)
    print(unique_status)

    return render(request, 'index.html', {"data": data})

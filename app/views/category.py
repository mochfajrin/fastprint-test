from app.models import Kategori
from django.shortcuts import render


def index(request):
    categories = Kategori.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'pages/dashboard/categories.html', context)

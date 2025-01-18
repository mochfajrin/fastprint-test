from django.shortcuts import render, redirect, get_object_or_404
from django.core import paginator
from app.api import fastprint
from app.helper.insert_fastprint import save_to_database


def index(request):
    save_to_database()
    return render(request, 'index.html')

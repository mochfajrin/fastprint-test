from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Max
from app.models import Kategori, Produk
from app.forms import KategoriCreateForm, KategoriUpdateForm


def index(request):
    categories = Kategori.objects.all().order_by("-id_kategori")
    ctx = {
        'categories': categories,
    }
    return render(request, 'pages/dashboard/categories.html', ctx)


def create(request):
    if (request.method == "POST"):
        next_id = Kategori.objects.aggregate(Max("id_kategori"))[
            "id_kategori__max"]
        next_id = (next_id or 0) + 1
        print(request.POST)
        form = KategoriCreateForm(request.POST)
        if (form.is_valid()):
            category = form.save(commit=False)
            category.id_kategori = next_id
            category.save()
            messages.success(request, "Berhasil membuat kategori")
            return redirect("categories")
    else:
        form = KategoriCreateForm()
    context = {
        'form': form
    }
    return render(
        request,
        'pages/dashboard/categories/create.html',
        context
    )


def update(request, id_kategori):
    category = get_object_or_404(Kategori, id_kategori=id_kategori)

    if request.method == "POST":
        form = KategoriUpdateForm(request.POST)

        if form.is_valid():
            nama_kategori = form.cleaned_data["nama_kategori"]
            if nama_kategori:
                category.nama_kategori = nama_kategori
            category.save()
            messages.success(request, "Berhasil memperbarui kategori")
            return redirect('categories')
    else:
        form = KategoriUpdateForm(initial={
            'nama_kategori': category.nama_kategori,
        })
    return render(
        request,
        "pages/dashboard/categories/edit.html",
        {
            'form': form,
            'id_kategori': id_kategori
        }
    )


def delete(request, id_kategori):
    category = get_object_or_404(Kategori, id_kategori=id_kategori)
    Produk.objects.filter(kategori_id=id_kategori).delete()
    category.delete()
    messages.success(request, "Berhasil menghapus kategori dan produk")
    return redirect("categories")

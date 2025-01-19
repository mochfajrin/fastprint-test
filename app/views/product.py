from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from django.contrib import messages
from app.helper.fastprint import save_to_database
from app.models import Produk
from app.forms import ProdukCreateForm, ProdukUpdateForm


def index(request):
    status = request.GET.get("status")
    products = []
    if status:
        products = Produk.objects.filter(
            status_id=int(status)).order_by("-id_produk")
    else:
        products = Produk.objects.all().order_by("-id_produk")
    ctx = {
        'products': products,
        'meta': {
            'status': status
        }
    }
    return render(request, 'pages/dashboard/products.html', ctx)


def create(request):
    if (request.method == "POST"):
        next_id = Produk.objects.aggregate(Max("id_produk"))["id_produk__max"]
        next_id = (next_id or 0) + 1
        form = ProdukCreateForm(request.POST)
        if (form.is_valid()):
            product = form.save(commit=False)
            product.id_produk = next_id
            product.save()
            messages.success(request, "Berhasil membuat produk")
            return redirect("products")
    else:
        form = ProdukCreateForm()
    context = {
        'form': form
    }
    return render(
        request,
        'pages/dashboard/products/create.html',
        context
    )


def update(request, id_produk):
    produk = get_object_or_404(Produk, id_produk=id_produk)

    if request.method == "POST":
        form = ProdukCreateForm(request.POST)

        if form.is_valid():
            nama_produk = form.cleaned_data["nama_produk"]
            harga = form.cleaned_data["harga"]
            kategori = form.cleaned_data['kategori']
            status = form.cleaned_data['status']
            if nama_produk:
                produk.nama_produk = nama_produk

            if harga:
                produk.harga = harga

            if kategori:
                produk.kategori = kategori

            if status:
                produk.status = status

            produk.save()
            messages.success(request, "Berhasil memperbarui produk")
            return redirect('products')
    else:
        form = ProdukUpdateForm(initial={
            'nama_produk': produk.nama_produk,
            'harga': produk.harga,
            'kategori': produk.kategori,
            'status': produk.status,
        })
    return render(
        request,
        "pages/dashboard/products/edit.html",
        {
            'form': form,
            'id_produk': id_produk
        }
    )


def delete(request, id_produk):
    product = get_object_or_404(Produk, id_produk=id_produk)
    product.delete()
    messages.success(request, "Berhasil menghapus produk")
    return redirect("products")


def fetch_products(request):
    if request.method == "GET":
        save_to_database()
        messages.success(request, "Berhasil mengambil data dari API")
        return redirect('products')

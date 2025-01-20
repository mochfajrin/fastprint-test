from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Max
from app.models import Status, Produk
from app.forms import StatusCreateForm, StatusUpdateForm


def index(request):
    status = Status.objects.all().order_by("-id_status")
    ctx = {
        'status': status,
    }
    return render(request, 'pages/dashboard/status.html', ctx)


def create(request):
    if (request.method == "POST"):
        next_id = Status.objects.aggregate(Max("id_status"))[
            "id_status__max"]
        next_id = (next_id or 0) + 1
        form = StatusCreateForm(request.POST)
        if (form.is_valid()):
            status = form.save(commit=False)
            status.id_status = next_id
            status.save()
            messages.success(request, "Berhasil membuat status")
            return redirect("status")
    else:
        form = StatusCreateForm()
    context = {
        'form': form
    }
    return render(
        request,
        'pages/dashboard/status/create.html',
        context
    )


def update(request, id_status):
    status = get_object_or_404(Status, id_status=id_status)

    if request.method == "POST":
        form = StatusUpdateForm(request.POST)

        if form.is_valid():
            nama_status = form.cleaned_data["nama_status"]
            if nama_status:
                status.nama_status = nama_status
            status.save()
            messages.success(request, "Berhasil memperbarui status")
            return redirect('status')
    else:
        form = StatusUpdateForm(initial={
            'nama_status': status.nama_status,
        })
    return render(
        request,
        "pages/dashboard/status/edit.html",
        {
            'form': form,
            'id_status': id_status
        }
    )


def delete(request, id_status):
    status = get_object_or_404(Status, id_status=id_status)
    Produk.objects.filter(status_id=id_status).delete()
    status.delete()
    messages.success(request, "Berhasil menghapus status dan produk")
    return redirect("status")

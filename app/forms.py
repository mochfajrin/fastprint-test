from django import forms
from app.models import Produk, Kategori, Status


class ProdukCreateForm(forms.ModelForm):
    id_produk = forms.IntegerField(required=False)
    nama_produk = forms.CharField(min_length=3, max_length=255, widget=forms.TextInput(attrs={
        'placeholder': "Masukkan nama produk",
        'class': "form-control",
    }), error_messages={
        'required': "Nama produk harus diisi",
        "max_length": "Nama produk maksimal 255 karakter",
        "max_length": "Nama produk minimal 3 karakter",
    })
    harga = forms.FloatField(widget=forms.NumberInput(attrs={
        'placeholder': "Masukkan harga",
        'class': "form-control",
    }), error_messages={
        'required': "Harga produk harus diisi",
        'invalid': "Harga harus berupa angka",
    })
    kategori = forms.ModelChoiceField(
        queryset=Kategori.objects.all(),
        to_field_name="id_kategori",
        widget=forms.Select(attrs={
            "class": "form-select",
            "id": "categoriesSelect"
        }), error_messages={
            "required": "Kategori harus diisi",
            "invalid_choice": "Pilihan tidak valid",
        }
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        to_field_name="id_status",
        widget=forms.Select(attrs={
            "class": "form-select"
        }),
        error_messages={
            "required": "Kategori harus diisi",
            "invalid_choice": "Pilihan tidak valid",
        }
    )

    class Meta:
        model = Produk
        fields = [
            "id_produk",
            "nama_produk",
            "harga",
            "kategori",
            "status",
        ]


class ProdukUpdateForm(forms.ModelForm):
    id_produk = forms.IntegerField(required=False)
    nama_produk = forms.CharField(required=False, min_length=3, max_length=255, widget=forms.TextInput(attrs={
        'placeholder': "Masukkan nama produk",
        'class': "form-control",
    }), error_messages={
        'required': "Nama produk harus diisi",
        "max_length": "Nama produk maksimal 255 karakter",
        "max_length": "Nama produk minimal 3 karakter",
    })
    harga = forms.FloatField(required=False, widget=forms.NumberInput(attrs={
        'placeholder': "Masukkan harga",
        'class': "form-control",
    }), error_messages={
        'required': "Harga produk harus diisi",
        'invalid': "Harga harus berupa angka",
    })
    kategori = forms.ModelChoiceField(
        required=False,
        queryset=Kategori.objects.all(),
        to_field_name="id_kategori",
        widget=forms.Select(attrs={
            "class": "form-select",
            "id": "categoriesSelect"
        }), error_messages={
            "required": "Kategori harus diisi",
            "invalid_choice": "Pilihan tidak valid",
        }
    )
    status = forms.ModelChoiceField(
        required=False,
        queryset=Status.objects.all(),
        to_field_name="id_status",
        widget=forms.Select(attrs={
            "class": "form-select"
        }),
        error_messages={
            "required": "Kategori harus diisi",
            "invalid_choice": "Pilihan tidak valid",
        }
    )

    class Meta:
        model = Produk
        fields = [
            "id_produk",
            "nama_produk",
            "harga",
            "kategori",
            "status",
        ]


class KategoriCreateForm(forms.ModelForm):
    nama_kategori = forms.CharField(min_length=3, max_length=255, widget=forms.TextInput(attrs={
        'placeholder': "Masukkan nama kategori",
        'class': "form-control",
    }), error_messages={
        'required': "Nama kategori harus diisi",
        "max_length": "Nama kategori maksimal 255 karakter",
        "max_length": "Nama kategori minimal 3 karakter",
    })

    class Meta:
        model = Kategori
        fields = [
            "nama_kategori",
        ]


class KategoriUpdateForm(forms.ModelForm):
    nama_kategori = forms.CharField(required=False, min_length=3, max_length=255, widget=forms.TextInput(attrs={
        'placeholder': "Masukkan nama kategori",
        'class': "form-control",
    }), error_messages={
        'required': "Nama kategori harus diisi",
        "max_length": "Nama kategori maksimal 255 karakter",
        "max_length": "Nama kategori minimal 3 karakter",
    })

    class Meta:
        model = Kategori
        fields = [
            "nama_kategori",
        ]


class StatusCreateForm(forms.ModelForm):
    nama_status = forms.CharField(min_length=3, max_length=255, widget=forms.TextInput(attrs={
        'placeholder': "Masukkan nama status",
        'class': "form-control",
    }), error_messages={
        'required': "Nama status harus diisi",
        "max_length": "Nama status maksimal 255 karakter",
        "max_length": "Nama status minimal 3 karakter",
    })

    class Meta:
        model = Status
        fields = [
            "nama_status",
        ]


class StatusUpdateForm(forms.ModelForm):
    nama_status = forms.CharField(required=False, min_length=3, max_length=255, widget=forms.TextInput(attrs={
        'placeholder': "Masukkan nama status",
        'class': "form-control",
    }), error_messages={
        'required': "Nama status harus diisi",
        "max_length": "Nama status maksimal 255 karakter",
        "max_length": "Nama status minimal 3 karakter",
    })

    class Meta:
        model = Status
        fields = [
            "nama_status",
        ]

from django.db import models


class Kategori(models.Model):
    id_kategori = models.BigIntegerField(primary_key=True)
    nama_kategori = models.CharField(255)

    class Meta:
        db_table = "kategori"


class Status(models.Model):
    id_status = models.BigIntegerField(primary_key=True)
    nama_status = models.CharField(255)

    class Meta:
        db_table = "status"


class Produk(models.Model):
    id_produk = models.BigAutoField(primary_key=True)
    nama_produk = models.CharField(255)
    harga = models.DecimalField(max_digits=6, decimal_places=2)
    kategori = models.ForeignKey(
        Kategori,
        on_delete=models.CASCADE,
        blank=False
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        blank=False
    )

    class Meta:
        db_table = "produk"

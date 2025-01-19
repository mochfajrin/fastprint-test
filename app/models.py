from django.db import models


class Kategori(models.Model):
    id_kategori = models.BigIntegerField(
        primary_key=True, editable=False, unique=True, db_index=True)
    nama_kategori = models.CharField(255)

    def __str__(self):
        return self.nama_kategori

    class Meta:
        db_table = "kategori"


class Status(models.Model):
    id_status = models.BigIntegerField(primary_key=True, db_index=True)
    nama_status = models.CharField(255)

    def __str__(self):
        return self.nama_status

    class Meta:
        db_table = "status"


class Produk(models.Model):
    id_produk = models.BigAutoField(primary_key=True, db_index=True)
    nama_produk = models.CharField()
    harga = models.FloatField()
    kategori = models.ForeignKey(
        Kategori,
        on_delete=models.CASCADE,
        blank=False,
        db_column="id_kategori"
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        blank=False,
        db_column="id_status"
    )

    class Meta:
        db_table = "produk"

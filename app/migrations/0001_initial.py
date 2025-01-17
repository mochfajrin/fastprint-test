# Generated by Django 5.1.5 on 2025-01-17 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(verbose_name=255)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_status', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nama_status', models.CharField(verbose_name=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id_produk', models.BigAutoField(primary_key=True, serialize=False)),
                ('nama_produk', models.CharField(verbose_name=255)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=6)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kategori')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.status')),
            ],
        ),
    ]

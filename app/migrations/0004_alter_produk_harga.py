# Generated by Django 4.2.18 on 2025-01-18 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_produk_kategori_alter_produk_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='harga',
            field=models.FloatField(),
        ),
    ]

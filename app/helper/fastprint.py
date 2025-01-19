from app.api import fastprint
from app.models import Kategori, Status, Produk


def save_to_database():
    products = fastprint.get_products()
    unique_categories = sorted(
        set(product["kategori"] for product in products))
    unique_status = sorted(set(product["status"] for product in products))

    categories = [
        {"id": index + 1, "nama_kategori": category}
        for index, category in enumerate(unique_categories)
    ]

    status = [
        {"id": index + 1, "nama_status": status}
        for index, status in enumerate(unique_status)
    ]

    products_object = []
    for product in products:
        for stat in status:
            if stat['nama_status'] == product['status']:
                product["status_id"] = stat["id"]

        for category in categories:
            if category['nama_kategori'] == product['kategori']:
                product["kategori_id"] = category["id"]

        del product['status']
        del product['kategori']
        del product['no']

        product['id_produk'] = int(product['id_produk'])
        product['harga'] = float(product['harga'])
        products_object.append(
            Produk(**product)
        )

    categories_object = []
    for category in categories:
        categories_object.append(
            Kategori(
                id_kategori=category["id"],
                nama_kategori=category["nama_kategori"],
            )
        )

    status_object = []
    for stat in status:
        status_object.append(
            Status(
                id_status=stat["id"],
                nama_status=stat["nama_status"],
            )
        )

    Kategori.objects.bulk_create(
        categories_object,
        update_conflicts=True,
        unique_fields=["id_kategori"],
        update_fields=['nama_kategori']
    )
    Status.objects.bulk_create(
        status_object,
        update_conflicts=True,
        unique_fields=["id_status"],
        update_fields=['nama_status']
    )
    Produk.objects.bulk_create(
        products_object,
        update_conflicts=True,
        unique_fields=['id_produk'],
        update_fields=['nama_produk', "kategori_id", "status_id"]
    )

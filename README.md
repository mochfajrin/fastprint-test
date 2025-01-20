# Fast Print - Tes Junior Programmer

## Get Started

### Creating Virtual Environment

```sh
python -m venv venv
```

### Enter the Virtual Environment

- Windows

```powershell
venv\Scripts\activate
```

- Linux

```bash
source venv\bin\activate
```

### Install Dependency

```bash
pip install -r requirements.txt
```

### Create PostgreSQL Database

```sh
CREATE DATABASE <YOUR_DATABASE_NAME>;
```

### Create .env file

```sh
cp .env.example .env
```

### Configure .Env

```sh
# DATABASE CONFIG

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

### Run Database Migration

```sh
# apabila migration gagal karena value dari .env tidak terbarui
# tutup dan buat terminal baru

python manage.py makemigrations
python manage.py migrate
```

### Run Django Application

```sh
python manage.py runserver
```

## Screenshots

### Halaman Dashboard

![](docs/assets/image/products.png)

### Mengambil data dari API

![](docs/assets/image/consume-api.png)

### Form tambah data

![](docs/assets/image/create.png)

### Sukses menambahkan data

![](docs/assets/image/success-create.png)

### Filter data

![](docs/assets/image/for-sell.png)

![](docs/assets/image/not-for-sell.png)

### Form update data

![](docs/assets/image/update.png)

### konfirmasi hapus data pada Form update

![](docs/assets/image/confirm-delete-on-update.png)

### Konfirmasi Hapus Data

![](docs/assets/image/confirm-delete.png)

### Notifikasi Hapus Data

![](docs/assets/image/success-delete.png)

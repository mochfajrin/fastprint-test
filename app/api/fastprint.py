import requests
import hashlib
import datetime
from zoneinfo import ZoneInfo


def get_products():
    dt = datetime.datetime.now(tz=ZoneInfo(
        "Asia/Jakarta")) + datetime.timedelta(hours=1)
    hour = '{:02d}'.format(dt.hour)
    day = '{:02d}'.format(dt.day)
    month = '{:02d}'.format(dt.month)
    year = str(dt.year % 100).zfill(2)

    username = f'tesprogrammer{day}{month}{year}C{hour}'
    password = f'bisacoding-{day}-{month}-{year}'
    encrypted_password = hashlib.md5(password.encode("UTF-8")).hexdigest()

    api_url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'
    data = {
        "username": username,
        "password": encrypted_password
    }

    data = requests.post(api_url, data).json()["data"]

    return data

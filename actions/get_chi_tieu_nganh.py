
import requests
import json
from config import app_config
import re


def get_chi_tieu_nganh(text):
    # Call api qua flask
    res = requests.get(app_config.DOMAIN+'/api/lay-chi-tieu-nganh', params={
        'message': text
    }, headers={
        'content-type': 'application/json'})
    print(res)
    message = ""
    ten_nganh = None
    if res.status_code == 200:
        res_data = res.json()
        message = res_data['payload']
        ten_nganh = res_data['ten_nganh']

    # Trường hợp không tìm thấy ngành học
    elif res.status_code == 400:
        message = res.json()['payload']
    else:
        message = "Có lỗi khi tương tác với database vui lòng thử lại sau"

    return {
        "message": message,
        "ten_nganh": ten_nganh,
    }

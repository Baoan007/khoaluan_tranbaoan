
import requests
import json
from config import app_config
import re


def get_by_fields(text, field):
    # Call api qua flask
    res = requests.get(app_config.DOMAIN+'/api/lay-nganh-by-field', params={
        'message': text,
        'field': field,
    }, headers={
        'content-type': 'application/json'})
    message = ""
    ma_nganh = None
    if res.status_code == 200:
        res_data = res.json()
        message = res_data['payload']
        ma_nganh = res_data['ma_nganh']

    # Trường hợp không tìm thấy ngành học
    elif res.status_code == 400:
        message = res.json()['payload']
    else:
        message = "Có lỗi khi tương tác với database vui lòng thử lại sau"

    return {
        "message": message,
        "ma_nganh": ma_nganh,
    }

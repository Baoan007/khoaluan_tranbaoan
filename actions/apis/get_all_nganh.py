
import requests
import json
from config import app_config
import re


def get_all_nganh(text):
    # Call api qua flask
    res = requests.get(app_config.DOMAIN+'/api/lay-all-nganh', params={
        'message': text
    }, headers={
        'content-type': 'application/json'})
    print(res)
    message = ""
    if res.status_code == 200:
        res_data = res.json()
        message = res_data['payload']

    # Trường hợp không tìm thấy ngành học
    elif res.status_code == 400:
        message = res.json()['payload']
    else:
        message = "Có lỗi khi tương tác với database vui lòng thử lại sau"

    return {
        "message": message
    }

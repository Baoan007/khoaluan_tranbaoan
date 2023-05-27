# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#

import requests
import json


from rasa_sdk.events import SlotSet
from utils.utils import format_amount
from database.models.tuyen_sinh import TuyenSinh

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/my_khtn'
# db = SQLAlchemy(app)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:@localhost/my_khtn')
Session = sessionmaker(bind=engine)
session = Session()


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_show_time"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []


# class GetChitieuNganhAction(Action):
#     def __init__(self):
#         self.session = session

#     def name(self):
#         return "action_get_chitieu_nganh"

#     # Khi thay đổi code phải train lại model
#     def run(self, dispatcher, tracker, domain):
#         print("Lấy action và message")
#         print(tracker.latest_message)

#         nganh = "hi"
#         print(nganh)
#         message = tracker.latest_message['intent'].get('name')
#         print(message)
#         if message == 'ask_countries':
#             # Truy vấn cơ sở dữ liệu để lấy chỉ tiêu của ngành
#             result = self.session.query(
#                 TuyenSinh).filter_by(chi_tieu=nganh).first()

#             if result:
#                 chitieu = result.chi_tieu
#                 message = f"Chỉ tiêu ngành {nganh} là {chitieu}"
#             else:
#                 message = f"Không tìm thấy thông tin về ngành {nganh}"

#         dispatcher.utter_message(text=message)
#         return []


# class ActionGetChitieuNganh(Action):
#     def name(self) -> Text:
#         return "action_get_chitieu_nganh"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         nganh = tracker.get_slot('nganh')

#         # Truy vấn cơ sở dữ liệu để lấy chỉ tiêu của ngành
#         result = session.query(TuyenSinh).filter_by(ten_nganh=nganh).first()

#         if result:
#             chitieu = result.chi_tieu
#             message = f"Chỉ tiêu ngành {nganh} là {chitieu}"
#         else:
#             message = f"Không tìm thấy thông tin về ngành {nganh}"

#         dispatcher.utter_message(text=message)
#         return []


class SearchNganhHocAction(Action):
    def name(self) -> Text:
        return "action_search_nganh_hoc"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        print(text)
        print(tracker.__dict__)
        ten_nganh = tracker.get_slot("ten_nganh")
        print(ten_nganh)
        # khoa = tracker.get_slot("khoa")
        # ma_chuyen_nganh = tracker.get_slot("ma_chuyen_nganh")
        # chi_tieu = tracker.get_slot("chi_tieu")
        # hoc_phi = tracker.get_slot("hoc_phi")

        # Truy vấn cơ sở dữ liệu để tìm kiếm thông tin
        # Sử dụng các thông tin (ten_nganh, khoa, ma_chuyen_nganh, chi_tieu, hoc_phi) để tìm kiếm và lấy thông tin từ bảng tuyển sinh

        # Ví dụ: Giả sử tìm kiếm thông tin theo tên ngành
        if ten_nganh:
            # Thực hiện truy vấn để lấy thông tin từ bảng tuyển sinh
            # result = query_database(ten_nganh)
            # result = {"ten_nganh": ten_nganh, "khoa": "Khoa Sinh học",
            #           "ma_chuyen_nganh": "CH001", "chi_tieu": 100, "hoc_phi": 15000000}

            # nganh = "Sinh học"
            result = session.query(
                TuyenSinh).filter_by(ten_nganh=ten_nganh.lower()).first()

            if result:
                print("hello")
                print(result)
                message = f"Thông tin về ngành {result.ten_nganh}:"
                message += f"\n- Khoa: {result.khoa}"
                message += f"\n- Mã chuyên ngành: {result.ma_chuyen_nganh}"
                message += f"\n- Chỉ tiêu: {result.chi_tieu}"
                message += f"\n- Học phí dự kiến: {format_amount(result.hoc_phi_du_kien)} vnd"
                # message = f"Thông tin về ngành {ten_nganh}:\nKhoa: {result['khoa']}\nMã chuyên ngành: {result['ma_chuyen_nganh']}\nChỉ tiêu: {result['chi_tieu']}\nHọc phí dự kiến: {result['hoc_phi']}"
            else:
                message = f"Không tìm thấy thông tin về ngành {ten_nganh}"
        else:
            message = "Xin lỗi, tôi không thể tìm kiếm thông tin với các thông tin đã cho."

        dispatcher.utter_message(text=message)

        return []

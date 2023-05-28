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

import re
from rasa_sdk.events import SlotSet, AllSlotsReset
from utils.utils import format_amount
from database.models.tuyen_sinh import TuyenSinh
from config import app_config
from actions.get_nganh import get_nganh
from actions.get_chi_tieu_nganh import get_chi_tieu_nganh

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


# Tìm thông tin ngành thông qua message
class SearchNganhHocAction(Action):
    def name(self) -> Text:
        return "action_search_nganh_hoc"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Chạy hàm run")
        text = tracker.latest_message['text']
        # name_message = tracker.latest_message['intent'].get('name')
        # Có thể xử lí dạng api
        print(tracker.__dict__)
        ten_nganh = None
        res_nganh_hoc = get_nganh(text)
        print(res_nganh_hoc)
        # Bot gửi cho user
        dispatcher.utter_message(text=res_nganh_hoc['message'])

        # Lưu cho slot dùng cho các action khác
        # return [SlotSet("ten_nganh", ten_nganh)]
        SlotSet("ten_nganh", res_nganh_hoc['ten_nganh'])
        return []


class SearchNganhChiTieuAction(Action):
    def name(self) -> Text:
        return "action_search_nganh_hoc_chi_tieu"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Chạy hàm run")
        text = tracker.latest_message['text']
        # name_message = tracker.latest_message['intent'].get('name')
        # Có thể xử lí dạng api
        print(tracker.__dict__)
        ten_nganh = None
        res_nganh_hoc = get_chi_tieu_nganh(text)
        print(res_nganh_hoc)
        # Bot gửi cho user
        dispatcher.utter_message(text=res_nganh_hoc['message'])

        # Lưu cho slot dùng cho các action khác
        # return [SlotSet("ten_nganh", ten_nganh)]
        SlotSet("ten_nganh", res_nganh_hoc['ten_nganh'])
        return []


# Action hiển thị tất cả tên ngành trong database không dùng đến api
class ShowNganhAllNganhHocAction(Action):
    def name(self) -> Text:
        return "action_get_nganh_hoc"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tuyen_sinhs = session.query(
            TuyenSinh).all()
        message = f"Thông tin về ngành:\n"
        for ts in tuyen_sinhs:
            message += f"\n- {ts.ten_nganh}"
        dispatcher.utter_message(text=message+"\n")

        return []


class ActionSayShirtSize(Action):

    def name(self) -> Text:
        return "action_say_shirt_size"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        shirt_size = tracker.get_slot("shirt_size")
        print(shirt_size)
        if not shirt_size:
            dispatcher.utter_message(text="I don't know your shirt size.")
        else:
            dispatcher.utter_message(text=f"Your shirt size is {shirt_size}!")
        return []

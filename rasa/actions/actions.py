# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json


from rasa_sdk.events import SlotSet

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/my_khtn'
db = SQLAlchemy(app)


class GetChitieuNganhAction(Action):
    def __init__(self):
        self.session = db.session

    def name(self):
        return "action_get_chitieu_nganh"

    def run(self, dispatcher, tracker, domain):
        print("Lấy action và message")
        print(tracker.latest_message)

        nganh = tracker.get_slot('chi_tieu')

        # Truy vấn cơ sở dữ liệu để lấy chỉ tiêu của ngành
        result = self.session.query(
            TuyenSinh).filter_by(chi_tieu=nganh).first()

        if result:
            chitieu = result.chi_tieu
            message = f"Chỉ tiêu ngành {nganh} là {chitieu}"
        else:
            message = f"Không tìm thấy thông tin về ngành {nganh}"

        dispatcher.utter_message(text=message)
        return [SlotSet('nganh', nganh)]

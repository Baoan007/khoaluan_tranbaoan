
from tkinter import EventType
from typing import Any, Text, Dict, List
from rasa_sdk.types import DomainDict

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
from actions.get_all_nganh import get_all_nganh

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:@localhost/my_khtn')
Session = sessionmaker(bind=engine)
session = Session()


class ActionTriggerResponseSelector(Action):
    """Returns the chatchit utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_trigger_response_selector"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        retrieval_intent = tracker.get_slot("retrieval_intent")
        if retrieval_intent:
            dispatcher.utter_message(template=f"utter_{retrieval_intent}")

        return [SlotSet("retrieval_intent", None)]

# ACTION xử lý cho các câu hỏi ngoại lệ
# USER_INTENT_OUT_OF_SCOPE = "out_of_scope"
# class ActionDefaultFallback(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> List[EventType]:

#         # Fallback caused by TwoStageFallbackPolicy
#         last_intent = tracker.latest_message["intent"]["name"]
#         if last_intent in ["nlu_fallback", USER_INTENT_OUT_OF_SCOPE]:
#             return [SlotSet("feedback_value", "negative")]

#         # Fallback caused by Core
#         else:
#             dispatcher.utter_message(template="utter_default")
#             return None

# Tìm thông tin ngành thông qua message
# Test thử lần đầu thì xuất ra được thông tin, hỏi lần 2 thì không
 # Test thêm Rule
# class SearchNganhHocAction(Action):
#     def name(self) -> Text:
#         return "action_search_nganh_hoc"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         print("Chạy hàm run")
#         text = tracker.latest_message['text']
#         # conversation_id = tracker.sender_id
#         # print(conversation_id)
#         # name_message = tracker.latest_message['intent'].get('name')
#         # Có thể xử lí dạng api
#         print(tracker.__dict__)
#         ten_nganh = None
#         res_nganh_hoc = get_nganh(text)
#         print(res_nganh_hoc)
#         # Bot gửi cho user
#         dispatcher.utter_message(text=res_nganh_hoc['message'])

#         # Lưu cho slot dùng cho các action khác
#         # return [SlotSet("ten_nganh", ten_nganh)]

#         return [SlotSet("ten_nganh", res_nganh_hoc['ten_nganh'])]


# class SearchNganhChiTieuAction(Action):
#     def name(self) -> Text:
#         return "action_search_nganh_hoc_chi_tieu"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         print("Chạy hàm run")
#         text = tracker.latest_message['text']
#         # name_message = tracker.latest_message['intent'].get('name')
#         # Có thể xử lí dạng api
#         print(tracker.__dict__)
#         ten_nganh = None
#         res_nganh_hoc = get_chi_tieu_nganh(text)
#         print(res_nganh_hoc)
#         # Bot gửi cho user
#         dispatcher.utter_message(text=res_nganh_hoc['message'])

#         # Lưu cho slot dùng cho các action khác
#         # return [SlotSet("ten_nganh", ten_nganh)]

#         return [SlotSet("ten_nganh", res_nganh_hoc['ten_nganh'])]


# Action hiển thị tất cả tên ngành trong database không dùng đến api
class ShowNganhAllNganhHocAction(Action):
    def name(self) -> Text:
        return "action_search_all_nganh_hoc"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tuyen_sinhs = session.query(
            TuyenSinh).all()
        message = f"Thông tin về ngành:\n"
        for ts in tuyen_sinhs:
            message += f"\n- {ts.ten_nganh}"
        dispatcher.utter_message(text=message+"\n")

        return []

# # Action hiển thị tất cả tên ngành trong database không dùng đến api
# class ShowNganhAllNganhHocAction(Action):
#     def name(self) -> Text:
#         return "action_search_all_nganh_hoc" #action_search_all_nganh_hoc

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         text = tracker.latest_message['text']
#         res_nganh_hoc = get_all_nganh(text)
#         dispatcher.utter_message(text=res_nganh_hoc['message']+"\n")

#         return []


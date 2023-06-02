from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
import json

import re
from rasa_sdk.events import SlotSet, AllSlotsReset
from utils.utils import format_amount
from database.models.tuyen_sinh import TuyenSinh
from config import app_config
from actions.apis.get_nganh import get_nganh
from actions.apis.get_chi_tieu_nganh import get_chi_tieu_nganh
from actions.apis.get_all_nganh import get_all_nganh


# Action hiển thị tất cả tên ngành trong database không dùng đến api
class ShowNganhAllNganhHocAction(Action):
    def name(self) -> Text:
        return "action_get_nganh_hoc"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        res_nganh_hoc = get_all_nganh(text)
        print(res_nganh_hoc)
        dispatcher.utter_message(text=res_nganh_hoc['message']+"\n")

        return []

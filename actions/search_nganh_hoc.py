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
from config import app_config
from actions.apis.get_nganh import get_nganh
from actions.apis.get_chi_tieu_nganh import get_chi_tieu_nganh


# Tìm thông tin ngành thông qua message
class SearchNganhHocAction(Action):
    def name(self) -> Text:
        return "action_search_nganh_hoc"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        res_nganh_hoc = get_nganh(text)
        dispatcher.utter_message(text=res_nganh_hoc['message'])

        return [SlotSet("ten_nganh", res_nganh_hoc['ten_nganh'])]


class SearchNganhChiTieuAction(Action):
    def name(self) -> Text:
        return "action_search_nganh_hoc_chi_tieu"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        res_nganh_hoc = get_chi_tieu_nganh(text)
        dispatcher.utter_message(text=res_nganh_hoc['message'])
        return [SlotSet("ten_nganh", res_nganh_hoc['ten_nganh'])]

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json

import re
from rasa_sdk.events import SlotSet, AllSlotsReset
from utils.utils import format_amount
from config import app_config
from actions.apis.get_nganh import get_nganh
from actions.apis.get_chi_tieu_nganh import get_chi_tieu_nganh
from actions.apis.get_nganh_by_fields import get_by_fields


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


class SearchNganhMaNganhAction(Action):
    def name(self) -> Text:
        return "action_search_nganh_hoc_ma_nganh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # # Đầu tiên người dùng sẽ hỏi mã ngành
        # # Bot sẽ phản hồi vui lòng nhập mã ngành
        # # Người dùng nhập mã ngành
        # # Từ mã ngành đó đi tìm luôn.
        # # Cũng không cần lưu slot làm gì
        text = tracker.latest_message['text']
        entities = tracker.latest_message.get('entities')
        # Kiểm tra xem entities có tồn tại và không rỗng
        if entities:
            for entity in entities:
                # Kiểm tra xem entity có là mã ngành hay không
                if entity['entity'] == 'ma_nganh':
                    ma_nganh = entity['value']

                    # Gửi thông tin về mã ngành cho người dùng
                    res_nganh_hoc = get_by_fields(text, ma_nganh)
                    dispatcher.utter_message(text=res_nganh_hoc['message'])

                    return [SlotSet("ma_nganh", ma_nganh)]
        # Nếu không tìm thấy mã ngành trong entities
        dispatcher.utter_message(
            text="Xin lỗi, không tìm thấy mã ngành. vui lòng tìm mã ngành khác")
        return []

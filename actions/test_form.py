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


class ActionSayShirtSize(Action):

    def name(self) -> Text:
        return "action_say_shirt_size"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        shirt_size = tracker.get_slot("shirt_size")
        if not shirt_size:
            dispatcher.utter_message(text="I don't know your shirt size.")
        else:
            dispatcher.utter_message(text=f"Your shirt size is {shirt_size}!")
        return []


class SetSlotAction(Action):
    def name(self) -> Text:
        return "action_set_slot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Lấy giá trị từ người dùng
        user_input = tracker.latest_message.get('text')
        # Set giá trị vào slot
        dispatcher.utter_message(f"Setting slot value to {user_input}")

        return [SlotSet("slot_name", user_input)]

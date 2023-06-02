from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted


class ActionRestartConversation(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic khởi động lại cuộc trò chuyện
        dispatcher.utter_message("Bắt đầu lại từ đầu. Xin chào!")
        return [Restarted()]

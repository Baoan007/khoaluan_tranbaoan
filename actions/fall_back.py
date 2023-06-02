from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted, Restarted, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher


class ActionFallback(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        # Xử lý fallback: Trả lời thông báo fallback
        dispatcher.utter_message("Xin lỗi, tôi không hiểu câu hỏi của bạn.")

        # Xóa các slot đã được set
        # return [AllSlotsReset()]
        # xóa sự kiện tạm thời để không infinity
        return [UserUtteranceReverted()]

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
# from typing import Text, List, Any, Dict

# from rasa_sdk import Tracker, FormValidationAction, Action
# from rasa_sdk.events import EventType
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict

# class ValidateSimplePizzaForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_info_form"

#     def validate_user_name(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `user_name` value."""
        
#         dispatcher.utter_message(text=f"OK! Rất vui khi được biết tên của bạn là {slot_value}.")
#         return {"user_name": slot_value}

#     def validate_user_old(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `user_old` value."""

#         dispatcher.utter_message(text=f"OK {slot_value} tuổi.")
#         return {"user_old": slot_value}
    
#     def validate_user_address(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `user_address` value."""

#         dispatcher.utter_message(text=f"Yead, quê của bạn là {slot_value}.")
#         return {"user_address": slot_value}

#     def validate_user_major(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `user_major` value."""

#         dispatcher.utter_message(text=f"Ngành học yêu thích của bạn là {slot_value}.")
#         return {"user_major": slot_value}

# class ActionTriggerResponseSelector(Action):
#     """Returns the chitchat utterance dependent on the intent"""

#     def name(self) -> Text:
#         return "action_trigger_response_selector"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[EventType]:
#         retrieval_intent = tracker.get_slot("retrieval_intent")
#         if retrieval_intent:
#             dispatcher.utter_message(template=f"utter_{retrieval_intent}")

#         return [SlotSet("retrieval_intent", None)]


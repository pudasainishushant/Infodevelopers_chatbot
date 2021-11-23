# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUtteranceReverted, AllSlotsReset
from rasa_sdk.forms import FormAction


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


class ActionGreet(Action):

    def name(self) -> Text:
        return "action_products"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        slot_value = tracker.get_slot("products")
        if slot_value:
            if slot_value == "mdabali":
                dispatcher.utter_message(response="utter_about_mdabali")
            elif slot_value == "infinity":
                dispatcher.utter_message(response="utter_about_infinity")
            elif slot_value == "empower":
                dispatcher.utter_message(response="utter_about_empower")
            elif slot_value == "wealth":
                dispatcher.utter_message(response="utter_about_wealth")
            elif slot_value == "budget management system":
                dispatcher.utter_message(response="utter_about_budget_management_system")
            elif slot_value == "online recruitment management system":
                dispatcher.utter_message(response="utter_about_online_recruitment_system")
            elif slot_value == "e-reconciliation system":
                dispatcher.utter_message(response="utter_about_e_reconciliation_system")
            elif slot_value == "human resource information system":
                dispatcher.utter_message(response="utter_about_human_resource_information_system")
            elif slot_value == "chatbot":
                dispatcher.utter_message(response="utter_about_chatbot_software")
            elif slot_value == "face based attendance system":
                dispatcher.utter_message(response="utter_about_face_attendance_system")
        else:
            slot_value = tracker.get_slot("features")
            if slot_value == "any branch banking system":
                dispatcher.utter_message(response="utter_about_any_branch_banking_system")
            if slot_value == "inter branch transaction":
                dispatcher.utter_message(response="utter_about_inter_branch_transaction")
            if slot_value == "bank gl code":
                dispatcher.utter_message(response="utter_about_gl_code")
            if slot_value == "sub ledger":
                dispatcher.utter_message(response="utter_about_sub_ledger")
            if slot_value == "account group code":
                dispatcher.utter_message(response="utter_about_account_group_code")
            if slot_value == "in transit gl":
                dispatcher.utter_message(response="utter_about_transit_gl")
            if slot_value == "operation code":
                dispatcher.utter_message(response="utter_about_operation_code")
            if slot_value == "pinned message":
                dispatcher.utter_message(response="utter_about_pinned_message")
        return [AllSlotsReset()]
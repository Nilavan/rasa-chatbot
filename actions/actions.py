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

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionShowLanguageOptions(Action):
#     def name(self) -> Text:
#         return "action_show_language_options"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_greet")
#         return []

# class ActionShowMainMenu(Action):
#     def name(self) -> Text:
#         return "action_show_main_menu"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_main_menu_eng")
#         return []

# class ActionDownloadAppInstructions(Action):
#     def name(self) -> Text:
#         return "action_download_app_instructions"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_app_download_instructions")
#         return []

# class ActionAskAnythingElse(Action):
#     def name(self) -> Text:
#         return "action_ask_anything_else"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_anything_else")
#         return []

# class ActionHandleLanguageChoice(Action):
#     def name(self) -> Text:
#         return "action_handle_language_choice"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         language = tracker.get_slot("language")
#         # Perform actions based on the selected language
#         dispatcher.utter_message(f"Selected language: {language}")
#         return []

# class ActionHandleDownloadChoice(Action):
#     def name(self) -> Text:
#         return "action_handle_download_choice"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         choice = tracker.get_slot("choice")
#         if choice == "Yes":
#             dispatcher.utter_message(template="utter_download_app")
#         else:
#             dispatcher.utter_message(template="utter_main_menu")
#         return []

# class ActionHandleAnythingElseChoice(Action):
#     def name(self) -> Text:
#         return "action_handle_anything_else_choice"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         choice = tracker.get_slot("choice")
#         if choice == "Yes":
#             dispatcher.utter_message(template="utter_main_menu")
#         else:
#             dispatcher.utter_message(template="utter_goodbye")
#         return []
        
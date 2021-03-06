# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import actions.SyllabusParser


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionRetrieveInstructor(Action):

    def name(self) -> Text:
        return "action_retrieve_instructor"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course = tracker.get_slot("course")
        # dispatcher.utter_message(text="Server Response: " + course)
        response = actions.SyllabusParser.find_instructor(course)
        dispatcher.utter_message(text=response)

        return []


class ActionRetrieveZoom(Action):

    def name(self) -> Text:
        return "action_retrieve_zoom"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course = tracker.get_slot("course")
        # dispatcher.utter_message(text="Server Response: " + course)
        response = actions.SyllabusParser.find_zoom(course)
        dispatcher.utter_message(text=response)

        return []


class ActionRetrievePrerequisites(Action):

    def name(self) -> Text:
        return "action_retrieve_prerequisites"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course = tracker.get_slot("course")
        # dispatcher.utter_message(text="Server Response: " + course)
        response = actions.SyllabusParser.find_prerequisites(course)
        dispatcher.utter_message(text=response)

        return []


class ActionRetrieveTextbook(Action):

    def name(self) -> Text:
        return "action_retrieve_textbook"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[
        Dict[Text, Any]]:
        course = tracker.get_slot("course")
        # dispatcher.utter_message(text="Server Response: " + course)
        response = actions.SyllabusParser.find_textbook(course)
        dispatcher.utter_message(text=response)

        return []


class ActionRetrieveEmail(Action):

    def name(self) -> Text:
        return "action_retrieve_email"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course = tracker.get_slot("course")
        #dispatcher.utter_message(text="Server Response: " + course)
        response = actions.SyllabusParser.find_email(course)
        dispatcher.utter_message(text=response)

        return []


class ActionRetrieveOffice(Action):

    def name(self) -> Text:
        return "action_retrieve_office"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course = tracker.get_slot("course")
        #dispatcher.utter_message(text="Server Response: " + course)
        response = actions.SyllabusParser.find_office(course)
        dispatcher.utter_message(text=response)

        return []


class ActionRetrievePhone(Action):

    def name(self) -> Text:
        return "action_retrieve_phone"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course = tracker.get_slot("course")
        #dispatcher.utter_message(text="Server Response: " + course)
        response = actions.SyllabusParser.find_phone(course)
        dispatcher.utter_message(text=response)

        return []
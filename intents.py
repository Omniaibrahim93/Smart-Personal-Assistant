import re
import webbrowser
import time
import platform

from actions import google_search, take_screenshot, lower_volume, raise_volume, lower_brightness, raise_brightness, start_word_project

from llm_client import ask_llm

class IntentAnalyzer:
    def __init__(self):
        self.intent_patterns = {
            "google_search": {
                "patterns": [
                    r"(?i)search (?:for )?(.+)",
                    r"(?i)google (.+)",
                    r"(?i)find (.+)"
                ]
            },
            "screenshot": {
                "patterns": [
                    r"(?i)(?:take |capture |save )?(?:a )?screenshot",
                    r"(?i)screen shot"
                ]
            },
            "volume_control": {
                "patterns": [
                    r"(?i)volume (up|down|increase|decrease)",
                    r"(?i)(mute|unmute) volume"
                ]
            },
            "brightness_control": {
                "patterns": [
                    r"(?i)(?:increase|raise|lower|decrease) brightness"
                ]
            },
            "open_word": {
                "patterns": [
                    r"(?i)open (?:microsoft )?word"
                ]
            }
        }
        self.compiled_patterns = {}
        for intent, data in self.intent_patterns.items():
            self.compiled_patterns[intent] = [re.compile(p) for p in data["patterns"]]

    def analyze_intent(self, user_input: str) -> dict:
        user_input = user_input.strip()
        for intent, patterns in self.compiled_patterns.items():
            for pattern in patterns:
                match = pattern.search(user_input)
                if match:
                    return {
                        "intent": intent,
                        "extracted_data": match.groups(),
                        "original_input": user_input
                    }
        return {
            "intent": "free_text",
            "extracted_data": (),
            "original_input": user_input
        }

    def execute_intent(self, intent_data: dict) -> str:
        intent = intent_data["intent"]
        extracted_data = intent_data["extracted_data"]
        original_input = intent_data["original_input"]

        if intent == "google_search":
            query = extracted_data[0] if extracted_data else original_input
            return google_search(query)
        elif intent == "screenshot":
            return take_screenshot()
        elif intent == "volume_control":
            command = extracted_data[0].lower() if extracted_data else ""
            if command in ["up", "increase"]:
                return raise_volume()
            elif command in ["down", "decrease"]:
                return lower_volume()
            elif command == "mute":
                # Implement mute if needed
                return "Volume muted (feature not implemented)"
            elif command == "unmute":
                return "Volume unmuted (feature not implemented)"
            else:
                return "Volume control command received"
        elif intent == "brightness_control":
            command = original_input.lower()
            if "increase" in command or "raise" in command:
                return raise_brightness()
            elif "lower" in command or "decrease" in command:
                return lower_brightness()
            else:
                return "Brightness control command received"
        elif intent == "open_word":
            return start_word_project()
        elif intent == "free_text":
            return ask_llm(original_input)
        else:
            return "Sorry, I didn't understand that command."

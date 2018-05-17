#!/usr/bin/env python3

import json
import requests

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class WeatherAction(Action):
    TEMPLATE = "The weather condition right now for {} is :: {}"
    def name(self):
        return 'action_weather'

    def _get_weather(self, url):
        response = requests.get(url)
        status = response.status_code
        data = json.loads(response.text)
        if status != 404:
            return data['weather'][0]['description'] if data else ""
        else:
            return ""

    def run(self, dispatcher, tracker, domain):
        api_key = "a9a88636051c1d2696509f00024370d0"
        location = tracker.get_slot('location')
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location, api_key)
        weather = self._get_weather(url)
        response = ""
        if not weather :
            response = "Sorry I cannot find the weather info for {}".format(location)
        else:
            response = WeatherAction.TEMPLATE.format(location, weather)
        dispatcher.utter_message(response)
        return [SlotSet('location', location)]


def main():
    weatheract = WeatherAction()

if __name__ == "__main__":
    main()


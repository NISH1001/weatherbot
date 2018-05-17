#!/usr/bin/env python3

import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter

def run_weather_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter('models/nlu/default/weathernlu')
    agent = Agent.load('models/dialogue', interpreter = interpreter)
    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent

def main():
    run_weather_bot()

if __name__ == "__main__":
    main()


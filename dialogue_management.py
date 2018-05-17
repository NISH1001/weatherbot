#!/usr/bin/env python3

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'weather_domain.yml',
                model_path = 'models/dialogue',
                training_data_file = 'data/stories.md'):

    agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy()])

    agent.train(
            training_data_file,
            max_history = 2,
            epochs = 10,
            batch_size = 50,
            validation_split = 0.2,
            augmentation_factor = 50)

    agent.persist(model_path)
    return agent

def run_weather_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter('models/nlu/default/weathernlu')
    agent = Agent.load('models/dialogue', interpreter = interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())

    return agent

def main():
    train_dialogue()
    run_weather_bot()

if __name__ == '__main__':
    main()
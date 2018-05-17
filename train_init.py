#!/usr/bin/env python3


import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

def main():
    logging.basicConfig(level='INFO')

    training_data_file = 'data/stories.md'
    model_path = 'models/dialogue'

    agent = Agent('weather_domain.yml', policies = [MemoizationPolicy(), KerasPolicy()])

    agent.train(
        training_data_file,
            augmentation_factor = 50,
            max_history = 2,
            epochs = 500,
            batch_size = 10,
            validation_split = 0.2)

    agent.persist(model_path)

if __name__ == "__main__":
    main()


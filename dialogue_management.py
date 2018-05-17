#!/usr/bin/env python3

import warnings
import sys

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'weather_domain.yml',
                model_path = 'models/dialogue',
                training_data_file = 'data/stories.md'):

    agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy()])

    agent.train(
            training_data_file,
            max_history = 2,
            epochs = 50,
            batch_size = 50,
            validation_split = 0.2,
            augmentation_factor = 50)

    agent.persist(model_path)
    return agent

def main():
    train_dialogue()

if __name__ == '__main__':
    main()

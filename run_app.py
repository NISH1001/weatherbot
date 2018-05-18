from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

import os

print("Downloading spacy model...")
os.system("python -m spacy download en")


print("Loading NLU model...")
nlu_interpreter = RasaNLUInterpreter('models/nlu/default/weathernlu')

print("Loading dialogue model...")
agent = Agent.load('models/dialogue', interpreter = nlu_interpreter)

print("Creating Slack input channel...")
input_channel = SlackInput("xoxp-365456006819-366603115687-365698335541-3fffd691b9e21872633ecb37c562c349",
                           "xoxb-365456006819-365016635361-7xdIR39l1KeKl5nRqKEZn7PZ",
                           "9kAwA9BgpiuuKdVnvQFyFKm8",
                           True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))

from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

import config
import os

config_auth = config.load_auth_config("config_auth.json")

print("Downloading spacy model...")
os.system("python -m spacy download en")


print("Loading NLU model...")
nlu_interpreter = RasaNLUInterpreter('models/nlu/default/weathernlu')

print("Loading dialogue model...")
agent = Agent.load('models/dialogue', interpreter = nlu_interpreter)

print("Creating Slack input channel...")
input_channel = SlackInput(config_auth['app_verification_token'],
                           config_auth['bot_verification_token'],
                           config_auth['slack_verification_token'],
                           True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))

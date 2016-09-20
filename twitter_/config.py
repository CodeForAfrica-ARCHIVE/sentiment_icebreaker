import os
import logging

LOGGING = {}
LOGGING['location'] = 'logs/log-streaming.log'
LOGGING['level'] = logging.DEBUG
LOGGING['format'] = '%(asctime)s : %(levelname)s: %(message)s'

PRINCIPLE_TW_HANDLE = 'pylitwoops'

TW_AUTH_CREDENTIALS = {}
TW_AUTH_CREDENTIALS['consumer_key'] = os.getenv('TW_CONSUMER_KEYS')
TW_AUTH_CREDENTIALS['consumer_secret'] = os.getenv('TW_CONSUMER_SECRETS')
TW_AUTH_CREDENTIALS['access_token_key'] = os.getenv('TW_ACCESS_TOKEN_KEYS')
TW_AUTH_CREDENTIALS['access_token_secret'] = os.getenv('TW_ACCESS_TOKEN_SECRETS')

SENDER_ID = {}
SENDER_ID['pylitwoops'] = '1237372231'

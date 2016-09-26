import os
import logging

LOGGING = {}
LOGGING['location'] = 'logs/log-streaming.log'
LOGGING['level'] = logging.DEBUG
LOGGING['format'] = '%(asctime)s : %(levelname)s: %(message)s'

PRINCIPLE_TW_HANDLE = 'pylitwoops'

TW_AUTH_CREDENTIALS = {}
TW_AUTH_CREDENTIALS['consumer_key'] = ""
TW_AUTH_CREDENTIALS['consumer_secret'] = ""
TW_AUTH_CREDENTIALS['access_token_key'] = ""
TW_AUTH_CREDENTIALS['access_token_secret'] = ""

import os
import logging

LOGGING = {}
LOGGING['location'] = 'logs/log-streaming.log'
LOGGING['level'] = logging.DEBUG
LOGGING['format'] = '%(asctime)s : %(levelname)s: %(message)s'

MESSAGESTORE = "/tmp/tweets-archive.txt"

PRINCIPLE_TW_HANDLE = ""

TW_AUTH_CREDENTIALS = {}
TW_AUTH_CREDENTIALS['consumer_key'] = ""   # Consumer Key (API Key)
TW_AUTH_CREDENTIALS['consumer_secret'] = ""   # Consumer Secret (API Secret)
TW_AUTH_CREDENTIALS['access_token_key'] = ""  # Access Token
TW_AUTH_CREDENTIALS['access_token_secret'] = ""  # Access Token Secret
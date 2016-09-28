import os
import logging

LOGGING = {}
LOGGING['location'] = 'logs/log-streaming.log'
LOGGING['level'] = logging.DEBUG
LOGGING['format'] = '%(asctime)s : %(levelname)s: %(message)s'

MESSAGESTORE = "/tmp/tweets-archive.txt"

PRINCIPLE_TW_HANDLE = ""

TW_AUTH_CREDENTIALS = {}
TW_AUTH_CREDENTIALS['consumer_key'] = "QbN1OWG7h9gBi14wImgiiNwRM"   # Consumer Key (API Key)
TW_AUTH_CREDENTIALS['consumer_secret'] = "ui89uvLbfQd71DWreYO0mRU3pIzkq6VTCxDWZJje58sb5gSHGH"   # Consumer Secret (API Secret)
TW_AUTH_CREDENTIALS['access_token_key'] = "81811976-yIEbKSr8mP4FfnvrvcfqhVhFZ7NSwQ7D7x3cTxR9U"  # Access Token
TW_AUTH_CREDENTIALS['access_token_secret'] = "SKuFJmUIav3RTsjptreLz5YGaaCUolOLdm2LKUtiF2cCn"  # Access Token Secret

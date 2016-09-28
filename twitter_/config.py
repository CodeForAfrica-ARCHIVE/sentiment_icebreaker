import os
import logging

LOGGING = {}
LOGGING['location'] = 'logs/log-streaming.log'
LOGGING['level'] = logging.DEBUG
LOGGING['format'] = '%(asctime)s : %(levelname)s: %(message)s'

MESSAGESTORE = "/tmp/tweets-archive.txt"

PRINCIPLE_TW_HANDLE = ""

TW_AUTH_CREDENTIALS = {}
TW_AUTH_CREDENTIALS['consumer_key'] = "btcGeW5Z7lSJ5irfCyoWCWZin"   # Consumer Key (API Key)
TW_AUTH_CREDENTIALS['consumer_secret'] = "0JwSP9j2gV29ixIbVHBkvRkl4mmt8xArOCQcs6fS82E1JryaBu"   # Consumer Secret (API Secret)
TW_AUTH_CREDENTIALS['access_token_key'] = "1237372231-CNFppr2FRW8pHpRRLg9IpJWzwVwenzRsjlwHcc4"  # Access Token
TW_AUTH_CREDENTIALS['access_token_secret'] = "GUn3b0OQVPlR8fjNx2Ib2NuDPiGZYQH8GaKAb97qvSB62"  # Access Token Secret
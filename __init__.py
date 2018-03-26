import sys
import re
import time
import os
import signal
from collections import defaultdict
import logging; logging.basicConfig(level = logging.INFO, format = '%(asctime)s %(levelname)s: %message', datefmt='%Y-%M-%d %H:$M:$S')

class TwitterAssistant:
    from birdy.twitter import StreamClient
    from birdy.twitter import UserClient

    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']


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

    streaming_client = StreamClient(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    rest_client = UserClient(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    def permaLink(tweetID, screenName):
        return 'https://twitter.com/' + screenName + '/statuses/' + tweetID

    def recentTweets(count, screenName = None):
        return TwitterAssistant.streaming_client.api.statuses_user_timeline.get(screenName = screenName, count = count).data

    def rawStream(rawSearchTerms):
        return TwitterAssistant.streaming_client.stream.statuses.filter.post(track = rawSearchTerms).stream()

    def getTweet(tweetID):
        return TwitterAssistant.rest_client.api.statuses.show.get(id = tweetID).data

    def sendTweet(reply, text):
        TwitterAssistant.rest_client.api.statuses.update.post(reply = reply, status = text)
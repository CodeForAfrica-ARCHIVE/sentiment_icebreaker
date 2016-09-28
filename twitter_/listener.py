"""
Stream listener

polyglot download sentiment2.en
polyglot download embeddings2.en ner2.en
"""
import tweepy
from sentiment_icebreaker.twitter_ import config

from polyglot.detect import Detector
from polyglot.text import Text


def get_api(auth_only=False, multi=False):
    """
    auth_only: return the OauthHandler object if True; else return the API object
    multi:     return multiple API client objects (if available), else: only return one API client object
    """
    try:
        creds = config.TW_AUTH_CREDENTIALS
        auth = tweepy.OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
        auth.set_access_token(creds['access_token_key'], creds['access_token_secret'])
        if auth_only:
            return auth
        api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        return api
    except Exception, err:
        api_err = 'Cannot create API object: {}'.format(str(err))
        raise err


class Listener(tweepy.StreamListener):
    """
    instance of tweepy's StreamListener
    """
    def __init__(self, logger=None):
        super(Listener, self).__init__()
        self.logger = logger
        self.api = get_api()

    def on_direct_message(self, msg):
        """
        do this when a direct message comes through
        """
        dm = msg.direct_message
        payload = dict(request_id=dm['id_str'],
                  created_at=dm['created_at'],
                  sender_id=dm['sender_id_str'],
                  username=dm['sender']['screen_name'],
                  message=dm['text'])
        summ = 'DM - {request_id} | {username} | {message}'.format(
                **payload)
        self.logger.info(summ)

        # 1) retrieve message language here....
        msg_text = payload["message"]
        language_detector = Detector(msg_text)
        language = language_detector.language.name

        
        # 2) retrieve message polarity here...
        try:
            msg_polarity = Text(msg_text).polarity
        except ZeroDivisionError:
            msg_polarity = 0
        msg_sentiment = "neutral"
        if msg_polarity < 0:
            msg_sentiment = "negative"
        elif msg_polarity > 0:
            msg_sentiment = "positive"

        
        # 3) retrieve message entities here...
        msg_entities = []
        for entity in Text(msg_text).entities:
            msg_entities.append(entity)


        # 4) Send response message to user here...
        
        
        # 5) Write results to file...
        output = [str(msg_text), msg_polarity, msg_sentiment]
        with open(config.MESSAGESTORE, 'a') as writefile:
            writefile.write("%s," % str(output))
        self.logger.debug("%s saved" % payload["request_id"])

         


    def on_dropped_connection(self,):
        """
        do this when Twitter closes connection
        """
        print "You probably need to restart me"

    
    def on_error(self, status_code):
        """
        handles errors
        """
        if int(status_code) == 420:
            # handle rate limiting
            return False

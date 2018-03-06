# http://adilmoujahid.com/posts/2014/07/twitter-analytics/

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#put the following into .config file in this dir
def get_twitter_config(schema='default'):
    ES = {}
    config_search_order = [ '.config']
    configparser = __import__('ConfigParser')

    config = configparser.ConfigParser()
    config.read(config_search_order)
    import pdb; pdb.set_trace()

    access_token = config.get(schema, 'access_token')
    access_token_secret = config.get(schema, 'access_token_secret')
    consumer_key = config.get(schema, 'consumer_key')
    consumer_secret = config.get(schema, 'consumer_secret')

    return access_token, access_token_secret, consumer_key, consumer_secret
#Variables that contains the user credentials to access Twitter API 
access_token, access_token_secret, consumer_key, consumer_secret = get_twitter_config()

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])

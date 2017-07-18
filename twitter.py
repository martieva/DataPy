import twitterAuth
from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import functools
import time
from dateutil import parser
import calendar
from textblob import TextBlob
from botornot import BotOrNot

cnt = 100
auth = twitterAuth.authenticate()
api = API(auth)
bon = BotOrNot(auth)
def average(mapper, subject):
    return functools.reduce(lambda x, y: x + y, map(mapper, subject))/cnt
#Listener Class Override
class MyStreamListener(StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('tweets.json', 'a')
        super(MyStreamListener, self).__init__()

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            self.saveFile.write(data)
            self.saveFile.write('\n')
            return True
        else:
            self.saveFile.close()
            return False

companyNames = ['MetLife', 'LibertyMutual', 'StateFarm', 'Fidelity', 'WeAreFarmers', 'Aflac', 'JacksonNational']

for name in companyNames:
    isBot = bon.check_account(name);
    statusList = api.user_timeline(name)
    timestamps = list(map(lambda s: calendar.timegm(s.created_at.timetuple()), statusList))
    #dateRange = max(timestamps) - min(timestamps)
    activityRating = max(timestamps) - min(timestamps)
    public_tweets = api.search(name);
    public_sentiment = average(lambda x: TextBlob(x.text).sentiment.polarity, public_tweets)

    print(name, activityRating, public_sentiment)


#myStream = Stream(auth=api.auth, listener=MyStreamListener(time_limit=20))
#myStream.filter(track=['Coffee'])

#print(mapReduce(lambda x: TextBlob(x.text).sentiment.polarity, public_tweets))

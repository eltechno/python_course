import tweepy, json

access_token = ""
access_token_secret=""
consumer_key=""
consumer_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token=(access_token, access_token_secret)


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

# create streaming object and authenticate
l = MyStreamListener()
stream = tweepy.Stream(auth,l)

#this line filter twitter streams to capture data by eywords
stream.filter(track=['chile', 'Guatemala'])

import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(10)


# Generous bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    # if follower.name == 'Hans':
    #     follower.follow()
    #     break


# print(user.followers_count)
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

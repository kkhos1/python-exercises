# https://developer.twitter.com/ paste from keys and tokens tab, don't share keys.
# Twitter bot retweets from home timeline. Use with caution.
import tweepy
import time

auth = tweepy.OAuthHandler('paste_consumer_key', 'paste_consumer_secret')
auth.set_access_token('paste_access_token', 'paste_access_token_secret')

api = tweepy.API(auth)
user = api.me()

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.followers_count > 100:
        print(follower.name)
        break

#print(user.screen_name)

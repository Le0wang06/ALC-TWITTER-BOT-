# our team's implementation of the twitter bot. This is the most basic twitter bot. A template for starter. 

# importing useful libraries.

import tweepy
import time

# here you store your important information directly from you app on the twitter developer portal.
# Twitter API credentials

consumer_key = 'YourConsumerKey'
consumer_secret = 'YourConsumerSecret'

access_token = 'YourAccessToken'
access_token_secret = 'YourAccessTokenSecret'


# Authenticate to Twitter
# this is getting verified to do whatever you want to do with twitter. Such as asking request if your bot is following all the policies.

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# a method here 
# Function to tweet
def tweet(message):
    api.update_status(message) #update_status

# Main function
def main():
    while True:
        # Tweet something
        tweet("Hello, world! This is a test tweet from ALC BOT")
        time.sleep(3600) # 3600 second pause before redoing this while loop again. Therefore re tweet the same msg again. 1 hour pause.


if __name__ == "__main__":
    main()
    

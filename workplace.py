# twitter_bot/api.py

import tweepy
import logging

#logging is a way to track events happening. This can help us better organize our tasks
# https://docs.python.org/3/library/logging.html <------ direct library to the logging documentations

class TwitterBot:
    def __init__(self, auth):
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        logging.info("Twitter API initialized")

    def post_tweet(self, text):
        try:
            tweet = self.api.update_status(status=text)
            logging.info(f"Tweet posted: {tweet.text}")
            return tweet
        except tweepy.TweepError as e:
            logging.error(f"Error posting tweet: {e.reason}")
            return None

    def reply_to_tweet(self, text, tweet_id):
        try:
            tweet = self.api.update_status(status=text, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
            logging.info(f"Replied to tweet ID {tweet_id}: {tweet.text}")
            return tweet
        except tweepy.TweepError as e:
            logging.error(f"Error replying to tweet: {e.reason}")
            return None

    def retweet(self, tweet_id):
        try:
            retweet = self.api.retweet(id=tweet_id)
            logging.info(f"Retweeted tweet ID {tweet_id}")
            return retweet
        except tweepy.TweepError as e:
            logging.error(f"Error retweeting: {e.reason}")
            return None

    def follow_user(self, user_id):
        try:
            user = self.api.create_friendship(user_id=user_id)
            logging.info(f"Followed user ID {user_id}")
            return user
        except tweepy.TweepError as e:
            logging.error(f"Error following user: {e.reason}")
            return None

    def send_direct_message(self, user_id, text):
        try:
            dm = self.api.send_direct_message(recipient_id=user_id, text=text)
            logging.info(f"Sent DM to user ID {user_id}: {text}")
            return dm
        except tweepy.TweepError as e:
            logging.error(f"Error sending DM: {e.reason}")
            return None

    def like_tweet(self, tweet_id):
        try:
            tweet = self.api.create_favorite(id=tweet_id)
            logging.info(f"Liked tweet ID {tweet_id}")
            return tweet
        except tweepy.TweepError as e:
            logging.error(f"Error liking tweet: {e.reason}")
            return None

    def unlike_tweet(self, tweet_id):
        try:
            tweet = self.api.destroy_favorite(id=tweet_id)
            logging.info(f"Unliked tweet ID {tweet_id}")
            return tweet
        except tweepy.TweepError as e:
            logging.error(f"Error unliking tweet: {e.reason}")
            return None

    def get_user_timeline(self, user_id, count=10):
        try:
            tweets = self.api.user_timeline(user_id=user_id, count=count)
            logging.info(f"Retrieved timeline for user ID {user_id}")
            return tweets
        except tweepy.TweepError as e:
            logging.error(f"Error retrieving user timeline: {e.reason}")
            return None

    def get_home_timeline(self, count=10):
        try:
            tweets = self.api.home_timeline(count=count)
            logging.info("Retrieved home timeline")
            return tweets
        except tweepy.TweepError as e:
            logging.error(f"Error retrieving home timeline: {e.reason}")
            return None

    def get_followers(self, user_id, count=10):
        try:
            followers = self.api.followers(user_id=user_id, count=count)
            logging.info(f"Retrieved followers for user ID {user_id}")
            return followers
        except tweepy.TweepError as e:
            logging.error(f"Error retrieving followers: {e.reason}")
            return None

    def get_friends(self, user_id, count=10):
        try:
            friends = self.api.friends(user_id=user_id, count=count)
            logging.info(f"Retrieved friends for user ID {user_id}")
            return friends
        except tweepy.TweepError as e:
            logging.error(f"Error retrieving friends: {e.reason}")
            return None

    def get_user_details(self, user_id):
        try:
            user = self.api.get_user(user_id=user_id)
            logging.info(f"Retrieved details for user ID {user_id}")
            return user
        except tweepy.TweepError as e:
            logging.error(f"Error retrieving user details: {e.reason}")
            return None

    def search_tweets(self, query, count=10):
        try:
            tweets = self.api.search_tweets(q=query, count=count)
            logging.info(f"Search for '{query}' returned {len(tweets)} tweets")
            return tweets
        except tweepy.TweepError as e:
            logging.error(f"Error searching tweets: {e.reason}")
            return None

    def stream_tweets(self, track_keywords, on_status_callback):
        class StreamListener(tweepy.StreamListener):
            def on_status(self, status):
                on_status_callback(status)
                logging.info(f"Streamed tweet from {status.user.screen_name}: {status.text}")

            def on_error(self, status_code):
                logging.error(f"Stream error: {status_code}")
                if status_code == 420:
                    return False

        listener = StreamListener()
        stream = tweepy.Stream(auth=self.api.auth, listener=listener)
        logging.info(f"Started streaming for keywords: {track_keywords}")
        stream.filter(track=track_keywords, is_async=True)

    def unfollow_user(self, user_id):
        try:
            user = self.api.destroy_friendship(user_id=user_id)
            logging.info(f"Unfollowed user ID {user_id}")
            return user
        except tweepy.TweepError as e:
            logging.error(f"Error unfollowing user: {e.reason}")
            return None

    def get_trending_topics(self, woeid):
        try:
            trends = self.api.get_place_trends(id=woeid)
            logging.info(f"Retrieved trending topics for WOEID {woeid}")
            return trends
        except tweepy.TweepError as e:
            logging.error(f"Error retrieving trending topics: {e.reason}")
            return None

    def tweet_with_media(self, text, media_path):
        try:
            tweet = self.api.update_with_media(filename=media_path, status=text)
            logging.info(f"Tweeted with media from {media_path}: {text}")
            return tweet
        except tweepy.TweepError as e:
            logging.error(f"Error tweeting with media: {e.reason}")
            return None

    def delete_tweet(self, tweet_id):
        try:
            tweet = self.api.destroy_status(id=tweet_id)
            logging.info(f"Deleted tweet ID {tweet_id}")
            return tweet
        except tweepy.TweepError as e:
            logging.error(f"Error deleting tweet: {e.reason}")
            return None

    def block_user(self, user_id):
        try:
            user = self.api.create_block(user_id=user_id)
            logging.info(f"Blocked user ID {user_id}")
            return user
        except tweepy.TweepError as e:
            logging.error(f"Error blocking user: {e.reason}")
            return None

    def unblock_user(self, user_id):
        try:
            user = self.api.destroy_block(user_id=user_id)
            logging.info(f"Unblocked user ID {user_id}")
            return user
        except tweepy.TweepError as e:
            logging.error(f"Error unblocking user: {e.reason}")
            return None

    def mute_user(self, user_id):
        try:
            user = self.api.create_mute(user_id=user_id)
            logging.info(f"Muted user ID {user_id}")
            return user
        except tweepy.TweepError as e:
            logging.error(f"Error muting user: {e.reason}")
            return None

    def unmute_user(self, user_id):
        try:
            user = self.api.destroy_mute(user_id=user_id)
            logging.info(f"Unmuted user ID {user_id}")
            return user
        except tweepy.TweepError as e:
            logging.error(f"Error unmuting user: {e.reason}")
            return None

    def send_tweet_with_location(self, text, lat, long):
        try:
            tweet = self.api.update_status(status=text, lat=lat, long=long)
            logging.info(f"Tweeted from location ({lat}, {long}): {text}")
            return tweet
        except tweepy.TweepError as e:
            logging.error(f"Error tweeting with location: {e.reason}")
            return None

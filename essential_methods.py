#get the user by their Twitter name.
# Methods in this group enable you to search users with a filter criteria, fetch user details, and list the followers of any user, as long as that user account is public.

# the get_user will get be representing the @MikezGarcia.

user = api.get_user("MikezGarcia")

# the built in get_user will then have different attributes within it's library : Name, Description and Location.

print("User details:")
print(user.name)
print(user.description)
print(user.location)

#a special method "followers" that will get the followers of the user assigned. Assuming that the user has at least 20 follwers.

print("Last 20 Followers:")

# for each follower inside the user.followers lists.

for follower in user.followers():
    print(follower.name) # prints our the name. Or here It will print out 20 names that represent last 20 followers.



# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


#assuming we have already created an API object
#now lets follow someone on the twitter using your bot.
api.create_friendship("@username_that_you_want_to_add")

#very important access for this bot is the timeline. This will be shown below: 
# These methods deal with reading tweets, mentions, and retweets from your timeline or any other user’s timeline, as long as it’s public. 
timeline = api.home_timeline()


#with this timeline you can do many other things 


# you can mark any tweet as Liked or remove the Like mark if it was already added.

#using timeline you can easily access the most recent tweet and then like it. 

tweets = api.home_timeline(count=1)
tweet = tweets[0]  #within the Tweets you access the index "0" which is the first one. In this organized method list. It seems like 0 will represent the most recent.
print(f"Liking tweet {tweet.id} of {tweet.author.name}")

api.create_favorite(tweet.id) # this will be liking the tweet.
#tweet is the object so you could access the id by doing "tweet.id" and then also getting the "tweet.author", this will give you the author of the tweet but mostlikely an object or an element and this is why 
# we will use the .name method to find it's name.






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



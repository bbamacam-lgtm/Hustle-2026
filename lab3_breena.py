# Breena | Lab 3| Intro to Python 
# Ticket 1

username = "hustlecoder"

print(len(username))
# PREDICT: 11
# yes, it counted all correct characters


# Ticket 2

print(username[0])
print(username[len(username) - 1])
# PREDICT: h r
# it would be len(username) minus 1 since it is index number

# Ticket 3

welcome = "Welcome to Loop"
banner = welcome + " " + username
print(banner)

print(f"Welcome to Loop, @{username}!")

# PREDICT: they won't look identical
# f-string felt more easier to input 

# Ticket 4

# username[0] = "X"
# PREDICT: it will say error
#  username[0] = "X" TypeError: 'str' object does not support item assignment
# not being able to change a string since it is immutable

# Ticket 5
feed = ["coder", "programming", "computer"]
print(len(feed)) 
# PREDICT: 3
# it's a list 

# Ticket 6
feed.append("python")
print(feed)
# PREDICT: ['coder', 'programming', 'computer', 'python'] 4
# it counts begins at 0

# Ticket 7
feed.pop(0)
feed.sort()
print(feed)
# PREDICT: coder is removed, so it will be ['computer', 'programming', 'python'] 
# I used .pop to remove index and .sort to sort the list in alphabetical order

# Ticket 8  
profile = {"username" : "hustlecoder", "followers" : 200, "verified" : True }
print(profile["followers"])
# profile[0] # KeyError: 0
# PREDICT: 200
# they print the values 

# Ticket 9
profile["followers"] = 200 + 50
print(profile["followers"])
profile["bio"] = "I love coding!"
print(profile)
print(profile.get("age"))
# PREDICT: none when key is missing
# it doesn't give you an error when key is not found

# Ticket 10
print(f" @{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: First day at Loop")
# PREDICT: hustelcoder has 250 followers and 3 posts. Top post: First day at Loop
# f-string, dictionary len()
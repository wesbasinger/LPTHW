from sys import exit

print "Just when you thought it was safe..."
print "Python dictionaries are awesome."
me = {
	"name" : "Wes",
	"gender" : "male",
	"age": 32,
	"likes_tacos": True,
	"favorite_sports" : ["football", "basketball", "football"]
}
print "Dictionaries are defined by curly block"
print "braces."
print '''
Pretend the following code block is entered for you.
me = {
	"name" : "Wes",
	"gender" : "male",
	"age": 32,
	"likes_tacos": True,
	"favorite_sports" : ["football", "basketball", "football"]
}
Give the following command: print me
'''

prompt = raw_input(">>> ")

if prompt == "print me":
	print me
	print "Good job."
else:
	print "Not quite, try again."
	exit()

print "Now, let's just access a certain part of the dictionary."
print "Give this command: print me['favorite_sports']"

prompt = raw_input(">>> ")

if prompt == "print me['favorite_sports']":
	print me['favorite_sports']
	print "Good job."
else:
	print "Not quite."
	exit(0)

print "So basically, instead of accessing by index, you access"
print "by key."
print "You can also delete stuff, but you can read about that"
print "in the textbook chapter."

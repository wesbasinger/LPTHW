from sys import exit

favorite_player = "My favorite player of all time is Tony Romo."

print "This lesson was all about list methods."
print "List methods are super useful."

print "Consider that the following string has been"
print "defined for you."

print '''
favorite_player = "My favorite player of all time is Tony Romo."
'''
print "First, let's look at the split method.  It is usually"
print "applied to strings."

print "Enter this command: stuff = favorite_player.split(' ')"

prompt = raw_input(">>> ")

if prompt == "stuff = favorite_player.split(' ')":
	stuff = favorite_player.split(' ')
	print "Good job"
else:
	print "Nope. Try again."
	exit(0)

print 'Give this command: print stuff'

prompt = raw_input('>>> ')

if prompt == "print stuff":
	print stuff
else:
	print "Nope, try again."
	exit(0)


print '''
Pretend you've typed in this block of code...
while len(stuff) > 0:
	print stuff.pop()
	print "Current List: " + str(stuff)
Press Enter to see it run.
'''

raw_input()

while len(stuff) > 0:
	print stuff.pop()
	print "Current List: " + str(stuff)

print "pop takes the last element off the list and returns it to you."

print "I'm going to define another list for you."
print "song = ['raindrops', 'on', 'roses']"

song = ['raindrops', 'on', 'roses']
print "Give this command: '-'.join(song)"

prompt = raw_input(">>> ")

if prompt == "'-'.join(song)":
	print '-'.join(song)
	print "See what it did?"
else:
	print "Nope, not quite."

print "That'll be all for now."

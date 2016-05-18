print "This lesson introduces conditional statement."
print "Branching is a huge topic for computer science."
print "This is the second time you will use indented code"
print "blocks.  If statements are similar to functions in"
print "that they use a statement followed by a colon, with"
print "indented lines underneath."

print '''
Image the following code is entered in for you.

swallows = 10
amazons = 12
people = 22

if swallows < amazons:
	print "Amazons win!"

if amazons > people:
	print "Jungle beats people!"

if (swallows + amazons) == people:
	print "Birds equal people."
'''

print "What do you think will be the first line printed?"

prompt = raw_input(">>> ")

if prompt == "Amazons win!":
	print "Good job."
else:
	print "Nope, you got it wrong."

print "What do you think will be the second line printed?"

prompt = raw_input('>>> ')

if prompt == "Birds equal people.":
	print "Good job.  That middle if statement isn't true so it doesn't print."
else:
	print "Nope, you got it wrong."

print "Okay, I hope that was a little extra practice for you."
print "If statements are helpful, that's how I've been checking your answers"
print "all along."


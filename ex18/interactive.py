import sys

def add_one(x):
	print x + 1


print "Wahoo, we're on to one of the most exciting"
print "parts of Python... the function."
print "Zed gives a great definition.  This is from the"
print "exercise reading."
print "1. Functions name pieces of code the way variables"
print "name strings and numbers."
print "2. Functions take arguments the way you pass arguments"
print "on the command line."
print "3. Using 1 and 2 they let you make your own mini"
print "scripts or commands."

print "It would be hard for me to interactively let you enter"
print "a function, so I've defined one already for you."
print """
def add_one(x):
	print x + 1
"""
print "You call the function by writing it's name with"
print "parameters in parenthesis."

print "Give this command: add_one(1)"

prompt = str(raw_input('>>> '))

if prompt == "add_one(1)":
	add_one(1)
	print "See how it did that?"
else:
	print "Not quite, try again."
	sys.exit(0)

print "This time change the input to something else between 2 and 9."

prompt = str(raw_input('>>> '))

add_one(int(prompt[-2]))

print "Good job, that's it for now."

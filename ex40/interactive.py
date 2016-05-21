from sys import exit

print "This is point where things take a turn."
print "You can write some really great scripts and"
print "do awesome stuff, you've learned just about"
print "every major data type and most common pieces"
print "of syntax."
print "But, if you want to be a real programmer,"
print "and write applications and programs beyond"
print "simple utility scripts, you'll need to dive"
print "into object-oriented programming."
print "Press Enter when you're ready to read more."
raw_input()
print "The first step of OOP is using modules, which"
print "really are just other files that have your"
print "code in them. This is a great way to keep"
print "things organized."
print "I'll try as best I can to show you this in an"
print "interactive session."

print """
Imagine you have a file in the same directory as where
you are running this imaginary prompt.  The file is
called stairway_to_heaven.py

This is a variable inside that file.
first_line = 'Theres a lady who's sure'
There is also a function.
def sing_chorus():
	print 'And as we wind on down the road'
Import the module by giving this command.
import stairway_to_heaven
"""

prompt = raw_input('>>> ')

if prompt == "import stairway_to_heaven":
	print "Module successfully imported."
else:
	print "Nope, try again."
	exit(0)

print "Now let's call a property from the module."
print "Give this command: print stairway_to_heaven.first_line"

prompt = raw_input('>>> ')

if prompt == "print stairway_to_heaven.first_line":
	print "There's a lady who's sure"
else:
	print "Nope, not quite."
	exit(0)

print "Now let's access a method in the same way."
print "Give this command: stairway_to_heaven.sing_chorus()"

prompt = raw_input('>>> ')

if prompt == "stairway_to_heaven.sing_chorus()":
	print "And as we wind on down the road."
else:
	print "Not quite, try again."
	exit(0)

print "But object oriented programming goes beyond"
print "just modules.  You can also do what are called classes."

print "Classes create objects."

class Candy(object):

	def __init__(self, name):
		self.name = name

	def eat(self):
		print "All gone.  Yummy."

print """
This class has been defined for you.
class Candy(object):

	def __init__(self, name):
		self.name = name

	def eat(self):
		print "All gone.  Yummy."
Let's create an instance of candy.
Give this command: snickers = Candy('snickers')"""

prompt = raw_input(">>> ")

if prompt == "snickers = Candy('snickers')":
	print "Good job.  Object instantiated."
	snickers = Candy('snickers')
else:
	print "Not quite, try again."
	exit(0)

print "Let's call a method on snickers."
print "Give this command: snickers.eat()"

prompt = raw_input('>>> ')

if prompt == "snickers.eat()":
	snickers.eat()
else:
	print "Not quite, try again."
	exit(0)

print "That should be enough to get your feet wet."
print "If you're like me, it might take a while for"
print "this to sink in. But, maybe you're smarter."

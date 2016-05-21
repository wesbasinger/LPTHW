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

print '''
Imagine you have a file in the same directory as where
you are running this imaginary prompt.  The file is
called stairway_to_heaven.py

This is a variable inside that file.
first_line = "There's a lady who's sure"
There is also a function.
def sing_chorus():
	print "And as we wind on down the road"
Import the module by giving this command.
import stairway_to_heaven
'''

prompt = raw_input('>>> ')

if prompt == "import stairway_to_heaven":
	print "Module successfully imported."
else:
	print "Nope, try again."
	exit(0)

print "Now let's call a method from the module."
print "Give this command: print stairway_to_heaven.first_line"

prompt = raw_input('>>> ')

if prompt == "print stairway_to_heaven.first_line":
	print "There's a lady who's sure"
else:
	print "Nope, not quite."
	exit(0)

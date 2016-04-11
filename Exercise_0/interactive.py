import sys

print '''Welcome to the Python interactive shell.
You can get to this very useful utility on any system that has Python installed by typing "Python [enter] on the command line
or terminal.'''

print '''First, let's use Python as a simple calculator.  Input
'2 + 2' (without the quotes) and see what happens.'''

first_prompt = int(input(">>> "))

print first_prompt

print '''You should have seen four.  Python calculated
the result of adding two integers together for you.'''

print '''Now you try adding two numbers together.'''

try:
	second_prompt = int(input(">>> "))
except NameError:
	print "You must not be using integers.  Try again."
	second_prompt = int(input(">>> "))

print second_prompt

print '''There are so many uses for the interactive shell,
and we will continue to emulate it in further lessons to
help you learn how to use this valuable tool.'''

print '\n'

print '''Let's finish up with some logical comparisions.'''

print '''Compare 4 and 2 by typing '4 > 2'.  It should print True.'''

third_prompt = input(">>> ")
print third_prompt

if third_prompt != (4 > 2):
	print "Nope, you missed something."
	third_prompt = input(">>> ")
else:
	print "Good job."

print '''Now enter a false statement.'''

fourth_prompt = input(">>> ")

if fourth_prompt:
	print "Woops, not quite.  Try again."
else:
	print "Good job, that's all for now."
	sys.exit(0)

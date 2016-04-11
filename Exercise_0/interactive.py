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



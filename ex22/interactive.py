print "Let's just take a little quiz."
print "On this section, you were supposed to just review."

points = 0

def print_score():
	print "So far you have %d points." % points

print_score()

print '''
Here's your first question.  Which of the following
objects have we talked about so far?
a Strings
b Integers
b Functions
d All of the above
'''

answer = raw_input(">>> ")

if answer.lower() == "d":
	print "Good job!"
	points += 1
else:
	print "Nope, sorry."

print_score()

print '''
Here's another question.  T/F Strings can be enclosed by
double OR single quotes.
T
F
'''

answer = raw_input('>>> ')

if answer.upper() == "T":
	print "Good job!"
	points += 1
else:
	print "Nope, sorry."

print_score()

print '''
Here's another question. Will this command read a file?
file = open('somefile.txt')
yes
no
'''

answer = raw_input('>>> ')

if answer.lower() == "no":
	print "Good job!"
	points += 1
else:
	print "Nope, sorry."

print_score()

print '''
One last question.  What keyword makes a function 'give
back' a value and is frequently used at the end of a function?
'''

answer = raw_input('>>> ')

if answer.lower() == "return":
	print "Good job!"
	points += 1
else:
	print "Nope, sorry."

print_score()

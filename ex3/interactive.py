import sys

print "Welcome to the interactive shell simulator."
print "This time we'll look at some basic math operations"
print "that can be done with Python."
print "Most of these should be very familar to you, with the"
print "exception of only a few."

print "What would the statement below evaluate to?"
print ">>2 + 2"
prompt = int(raw_input(">>"))

if prompt == 4:
	print "Good job!"
else:
	print "Try again!"
	prompt = int(raw_input(">>"))

print "What would the statement below evaluate to?"
print ">>2.4 + 4.6"
prompt = float(raw_input(">>"))

if prompt == 7.0:
	print "Good job!"
else:
	print "Try again! Remember, floating points are different."
	prompt = int(raw_input(">>"))

print "What would the statement below evaluate to?"
print ">>2 * 9 + 1"
prompt = int(raw_input(">>"))

if prompt == 19:
	print "Good job!"
else:
	print "Try again! Remember, order of operations applies in Python."
	prompt = int(raw_input(">>"))

print "What would the statement below evaluate to?"
print ">>5 + 2 - 8 + 3 / 4"
prompt = int(raw_input(">>"))

if prompt == -1:
	print "Good job!"
else:
	print "Try again! Remember, order of operations applies in Python."
	prompt = int(raw_input(">>"))

print "What would the statement below evaluate to?"
print ">>10 % 2"
prompt = int(raw_input(">>"))

if prompt == 0:
	print "Good job!"
else:
	print "Try again! Remember, % stands for modular division."
	prompt = int(raw_input(">>"))

print "What would the statement below evaluate to?"
print ">>4 + 3 > 6"
prompt = str(raw_input(">>"))

if prompt == "True":
	print "Good job!"
else:
	print "Try again! This is a boolean, so your answer should be True or False."
	prompt = str(raw_input(">>"))

print "What would the statement below evaluate to?"
print ">>2*2 >= 2 + 4"
prompt = str(raw_input(">>"))

if prompt == "True":
	print "Good job!"
else:
	print "Try again! This is a boolean, so your answer should be True or False."
	prompt = str(raw_input(">>"))

print "What would the statement below evaluate to?"
print ">>11/3 < 3"
prompt = str(raw_input(">>"))

if prompt == "False":
	print "Good job!"
else:
	print "Try again! This is a boolean, so your answer should be True or False."
	prompt = str(raw_input(">>"))

print "You passed all successfully, no need to review basic math :-)"
exit(0)

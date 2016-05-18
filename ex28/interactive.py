print "I'm going to give you some more Boolean practice."
print "Like Zed says, it is an essential part of programming."

print "For each of the following, type what you think the result"
print "should be.  In other words, you should always enter either"
print "'True' or 'False' (without the quotes)."

points = 0

print "=================================="
print "Boolean statement: True and False"
print "=================================="

answer = raw_input("ANSWER: ")

if answer == "False":
	points += 1
	print "You got it."
else:
	print "Nope. Sorry."

print "=================================="
print "Boolean statement: False and False"
print "=================================="

answer = raw_input("ANSWER: ")

if answer == "False":
	points += 1
	print "You got it."
else:
	print "Nope, sorry."

print "=================================="
print "Boolean statement: True or True"
print "=================================="

answer = raw_input("ANSWER: ")

if answer == "True":
	points += 1
	print "You got it."
else:
	print "Nope, sorry."

print "=================================="
print "Boolean statement: 1 == 2 or 2 == 1"
print "=================================="

answer = raw_input("ANSWER: ")

if answer == "False":
	points += 1
	print "You got it."
else:
	print "Nope, sorry."

print "=================================="
print "Boolean statement: 'test' == 'test'"
print "=================================="

answer = raw_input("ANSWER: ")

if answer == "True":
	points += 1
	print "Good job."
else:
	print "Nope, not quite."

print "=================================="
print "Boolean statement: False or 3 == (5 - 2)"
print "=================================="

answer = raw_input("ANSWER: ")

if answer == "True":
	points += 1
	print "Good job."
else:
	print "Not quite."

print "=================================="
print "Boolean statement: 'test' != 'testing'"
print "=================================="

answer = raw_input("ANSWER: ")

if answer == "True":
	points += 1
	print "Good job."
else:
	print "Not quite."

print "=================================="
print "Boolean statement: 2 != 4 and 2 == 4"
print "=================================="

answer = raw_input("ANSWER: ")

if answer == "False":
	points += 1
	print "Good job."
else:
	print "Not quite."

print "=================================="
print "Boolean statement: 'string' == 'String'"
print "=================================="

answer = raw_input("ANSWER: ")

if answer == "False":
	points += 1
	print "Good job."
else:
	print "Not quite."

print "=================================="
print "Boolean statement: not (True and False)"
print "=================================="

answer = raw_input("ANSWER: ")

if answer == "True":
	points += 1
	print "Good job."
else:
	print "Not quite."

print "=================================="
print "Boolean statement: not ('round' == 'round' )"
print "=================================="

answer = raw_input("ANSWER: ")

if answer == "False":
	points += 1
	print "Good job."
else:
	print "Not quite."

print "Wow, you got %d total points." % points

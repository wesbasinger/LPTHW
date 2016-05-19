print "Okay, let's work with the branching a little more."
print "Sometimes a simple if statement is all you need, but"
print "you should know how to create multiple branches with"
print "elif and else."

print '''
Read the following code block and see if you know what
is going to happen.

witches = 10
bridges = 5
angry_villagers = 3

if witches < bridges:
	print "No way we can build that many bridges!"

elif witches = bridges:
	print "Maybe we can build one bridge."

else:
	print "We should be able to build at least one bridge."
'''

print '''
Which statement will print?
a No way we can build that many bridges!
b Maybe we can build one bridge.
c We should be able to build at least one bridge.
'''

prompt = raw_input("ANSWER: ")

if prompt == "c":
	print "Good job!"
else:
	print "Nope, not quite."

print '''
Consider this code block.

a = 4
b = 3

if a < b:
	print a
elif a > b:
	print a
else:
	print b

What will print?
'''

prompt = raw_input('ANSWER: ')

if prompt == '4':
	print "Good job!"
else:
	print "Not quite."

print "You can add as many elif's as you want."
print "Python syntax for branching is great."

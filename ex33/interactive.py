print "While loops are okay. Zed is right, for loops are"
print "used a lot more in the wild."

print "While loops follow the same sytax pattern of"
print "indentation."

print '''
Look at this code block.

number_of_kids_left = 9
while number_of_kids_left > 0:
	print "You have %d kids left." % number_of_kids_left
	number_of_kids -= 1
Press Enter to see it run.
'''

raw_input()

number_of_kids_left = 9
while number_of_kids_left > 0:
	print "You have %d kids left." % number_of_kids_left
	number_of_kids_left -= 1

print "It is vitally important that you decrement"
print "the counter variable in the loop, or else it"
print "will run forever.  Look at the next example,"
print "and how I've created a break in the code."

print '''

running = True

while running:
	print "1 to keep playing."
	print "2 to stop."
	prompt = raw_input()
	if prompt == 2:
		running = False
Press Enter to start.
'''

raw_input()

running = True

while running:
	print "1 to keep playing."
	print "2 to stop."
	prompt = str(raw_input())
	if prompt == "2":
		running = False

print '''
Here's a bad example.

witches = []

while True:
	witches.append("witch")
	print witches

Press Enter to see this run.
Ctrl C will kill it.
'''

raw_input()
witches = []

while True:
	witches.append("witch")
	print witches



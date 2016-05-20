print "This lesson introduces the idea of an index."
print "That's why order matters in a list, because"
print "you should be able to grab an element at any"
print "position."

print "Consider this list: fruits = ['apple', 'pear', 'grape']"
print '''
Which element of the list would you like to access?
0
1
2
'''

prompt = str(raw_input("Which index? "))

if prompt == "0":
	print "You get apple."
elif prompt == "1":
	print "You get pear."
elif prompt == "2":
	print "You get grape."
else:
	print "You didn't input a valid index."

print "Do it again."

prompt = str(raw_input("Which index? "))

if prompt == "0":
	print "You get apple."
elif prompt == "1":
	print "You get pear."
elif prompt == "2":
	print "You get grape."
else:
	print "You didn't input a valid index."

print '''
Okay, here's another list.  This time, access any element
of the weekend using proper syntax.
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
'''

prompt = str(raw_input(">>> "))

if prompt == "days[0]":
	print "Good job, Sunday is part of the weekend."
elif prompt == "days[6]":
	print "Good job, Saturday is part of the weekend."
else:
	print "Nope, try again."



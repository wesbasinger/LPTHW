print "I love lists, they were my favorite data"
print "structure before I discovered the next one"
print "you'll be learning about."
print "Lists are exactly what you think they would be."

print "Here's an example list."
print "[0, 1, 2, 3, 4]"
print "But those are just numbers."
print "It is helpful to define or name your lists."
print "my_pets = ['Johnny', 'Crosby', 'Olivia']"
print "The course will go into great detail later on lists."
print "For now, we are just going to learn how to iterate over"
print "a list. Python has the BEST syntax for traversing lists."
print "If you ever learn another language, you'll be mad it"
print "isn't this easy."

even_numbers = [2, 4, 6, 8, 10]

print '''
Pretend you run this bit of code.
even_numbers = [2, 4, 6, 8, 10]

for even in even_numbers:
	print even
Press Enter when  you're ready to see it run.
'''

raw_input()

for even in even_numbers:
	print even

family = ["Wes", "Amy", "Abby", "Annabelle", "Will", "Walter"]

print '''
You can do it with lists of strings as well.
Watch what this bit of code does.
family = ["Wes", "Amy", "Abby", "Annabelle", "Will", "Walter"]
for member in family:
	print "%s is in my family." % member
Press Enter to see it run.
'''

raw_input()

for member in family:
	print "%s is in my family." % member

print '''
You can even do it with ranges of numbers.
for i in range(0, 10):
	print "Element " + str(i)
Press Enter to see it run.
'''

raw_input()

for i in range(0,10):
	print "Element " + str(i)

print "You can also build lists using the for statement."
print "Pretend that you start with an empty list."
print "empty = []"
print '''
Watch what this code block does.
for i in range(1, 10):
	empty.append(i*i)
print empty
Press enter to watch it run.
'''

empty = []

raw_input()

for i in range(1, 10):
	empty.append(i*i)
print empty

print "And once more to prove the point."
print '''
This is the code block that will run.
for square in empty:
	print str(square) + " is a perfect square."
Press enter to see it run.
'''

raw_input()

for square in empty:
	print str(square) + " is a perfect square."

print "And that should give you a good idea of how it works."


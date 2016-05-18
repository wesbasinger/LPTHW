print '''
Ex 1 is all about the print command, which
is how you get things to print onto the screen.
Print is extremely helpful for debugging, and the
syntax is incredibily refreshing in Python.'''

user_input = str((raw_input("Give the command to print 'Hello World!'\n>>")))

if user_input == "print 'Hello World!'" or user_input == 'print "Hello World!"':
	print "Success!"
else:
	print "It's not matching exactly right."
	user_input = str((raw_input("Give the command to print 'Hello World!'\n>>")))

user_input = str((raw_input("Give the command to print 'Python is known to be a very productive language.'\n>> ")))

if user_input == "print 'Python is known to be a very productive language.'" or user_input == 'print "Python is known to be a very productive language."':
	print "Success!"
else:
	print "It's not matching exactly right."
	user_input = str((raw_input("Give the command to print 'Python is known to be a very productive language.'\n>>")))


user_input = str((raw_input("Give the command to print 'Python is great because it does garbage collection.'\n>> ")))

if user_input == "print 'Python is greate because it does garbage collection.'" or user_input == 'print "Python is great because it does garbage collection."':
	print "Success!"
else:
	print "It's not matching exactly right."
	user_input = str((raw_input("Give the command to print 'Python is great because it does garbage collection.'\n>>")))


user_input = str((raw_input("Give the command to print 'Python does not use curly braces for code blocks, instead it uses whitespace.'\n>> ")))

if user_input == "print 'Python does not use curly braces for code blocks, instead it uses whitespace.'" or user_input == 'print "Python does not use curly braces for code blocks, instead it uses whitespace."':
	print "Success!"
else:
	print "It's not matching exactly right."
	user_input = str((raw_input("Give the command to print 'Python does not use curly braces for code blocks, instead it uses whitespace.'\n>>")))

print "Great job, go ahead and try the practice.py exercise now."
exit(0)

print "This is not my favorite type of material,"
print "so the exercises will be fairly sparse here."

print "Here is a quote from Exercise 10."
print '''
This \ (backslash) character encodes difficult-to-type 
characters into a string. There are various escape 
sequences available for different characters 
you might want to use.'''

prompt = str(raw_input("Quick quiz, what is the escape character?"))

if prompt == '\\':
	print "Good job!"
else:
	print "Not quite, try again!"

prompt = str(raw_input('True or False: The escape character can escape multiple things?'))

if prompt == "True":
	print "Good job, that's all I've got."
else:
	print "Not quite, try again."

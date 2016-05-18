from sys import exit

print "This exercise is very much a duplication of the last one"
print "with one exception.  I call it string multiplication, not"
print "sure what it is really called."

print "Input the following command and see what happens."
print "'Hello'*3"

prompt = str(raw_input(">>>"))

delim = prompt.split("*")

if delim != ["'Hello'","3"]:
	print "You didn't input the command right."
	exit(0)

print "'HelloHelloHello'"

print '\n'

print "See what that does?"
print "Now you give the command to print 'five' 5 times."

prompt = str(raw_input(">>>"))

delim = prompt.split('*')

if delim != ["'five'", "5"]:
	print "You didn't input the command right."
	exit(0)
else:
	print "Success!"

print "Okay, now you try any type of string multiplication you want."

prompt = str(raw_input(">>>"))

delim = prompt.split('*')

print str(delim[0])*int(delim[1])

exit(0)

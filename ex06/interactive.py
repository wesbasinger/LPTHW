from sys import exit


print "String concatenation is useful.  Let's watch it in action."

print "Declare two variables, x = 'Spam' and y = 'Eggs'"

x = raw_input(">>>")
y = raw_input('>>>')

if (x[-5:-1]) != "Spam":
	print "You didn't declare the variable 'Spam'!"
	print "Try again!"
	exit(0)

if (y[-5:-1]) != 'Eggs':
	print "You didn't declare the variable 'Eggs'!"
	print "Try again!"
	exit(0)

print "Okay, the variables are stored.  Now, run"
print "this command. 'print x + y'"

cat = raw_input(">>>")

delim = cat.split(' ')

if delim == ['print', 'x', '+', 'y'] or 'x+y' in delim:
	print "SpamEggs"
	print "Good job, you did it!"

print "Sometimes, we would like to have a little space"
print "between our words.  We can add a space by"
print "giving a command like this:"
print "print x + ' ' + y"
print "Now you try..."

cat = raw_input('>>>')

if ('print' in cat) and ('x' in cat) and ("\' \'" in cat) and ('y' in cat):
	print "Spam Eggs"
	print "Success!"
	exit(0)
else:
	print "Try again!"
	exit(0)

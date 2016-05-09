print "Finally, we're out of the boring stuff!"
print "This lesson focuses on command line arguments,"
print "which are extremely handy for small programs"
print "When you only need to pass a few parameters in."

def say_hello(name):
	return "Hello " + name

print "Let's watch this in action.  Let's way I've written"
print "a program that takes one command line argument, your name."

print "Pretend you are on the command line.  Run this direction."
print "python say_hello.py 'Bob'"
prompt = raw_input('$')

delim = prompt.split(' ')

if delim == ['python', 'say_hello.py', "'Bob'"]:
	print say_hello('Bob')
	print "Good job!"

print "Now, you pick any name you like to go as the command line"
print "argument and see what happens."

prompt = raw_input('$')

delim = prompt.split(' ')
print say_hello(delim[-1])

print "Do you see how that works? It's because I'm using the arg in my small program."

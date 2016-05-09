from sys import exit

print "Bet you're sick of printing by now!"
print "But wait, there's more."

print "This lesson introduces two important concepts,"
print "the newline character and the multi line print statement."
print "I've seen the multi line print statement used more for"
print "long comments and docstrings, but it's still good to learn"
print "like this."

print "First, input this command, I'm not really going to check your"
print "basic inputs from now on, I think you should have those down"
print "by now."
print r'print "Hello\n"'
prompt = raw_input(">>>")

print "Did you see how it put in a new line?"
print r'The \n inserts a new line character.'
print "You don't see it too much in the shell,"
print "but you will when you start working with real files."

print "Now you try making a string that has a new line."
prompt = raw_input('>>>')

if r'\n' in prompt:
	print "Great job.  We wont belabor that point."

print "Multiline comments would be a bit of a pain to implement."
print "We'll catch those later."

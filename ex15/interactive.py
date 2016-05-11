print "I'm excited.  This is where stuff gets"
print "really fun.  We're going to start working"
print "with files."

print "Python makes working with files extremely easy."
print "I think it's fun, because it teaches you basic"
print "computer survival skills like file types and"
print "directory structure."

print "Enough talking, let's practice opening a file."
print "Pretend there is a file called 'holy.txt' in"
print "the current directory."

print "Give this command to make a pointer that opens"
print "the file."
print "'holy = open(\'holy.txt\')'"
prompt = str(raw_input(">>>"))

if prompt == 'holy = open(\'holy.txt\')':
	print "Success"
	print "Now give the command: 'holy.read()'"
	prompt = str(raw_input('>>>'))
	if prompt == "holy.read()":
		print "You've just opened the Holy Hand Grenade of Antioch."
	else:
		print "So close!  Try again"
		sys.exit(0)
else:
	print "Almost, try again!"

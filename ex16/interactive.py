from sys import exit
test_file = """
This is the first line of your test file.
This is the second line of your test file.
This is the last line of your test file.
"""


print "Okay, let's do a little more work with files."
print "I guess the new thing on this lesson is writing"
print "and being a little more specific about reading."

print "First, if you're a Mac or Linux user, there is a"
print "useful command called 'cat' which displays a file"
print "from the command line."
print "Give this command to see what is in 'test.txt'"
print "cat 'test.txt'"

prompt = str(raw_input("$"))

if prompt == "cat 'test.txt'":
	print test_file
	print "Right, now you see it has content."
else:
	print "Not quite, try again."
	exit(0)

print "Now let's erase that file."
print "First, we have to open it."
print "Give this command: target = open('test.txt')"

prompt = str(raw_input(">>>"))

if prompt == "target = open('test.txt')":
	print "Good job, you now have a file pointer object."
else:
	print "Not quite, try again."
	exit(0)

print "Okay, let's erase the file with truncate()"
print "Give this command: target.truncate()"

prompt = str(raw_input("$"))

if prompt == "target.truncate()":
	print "Good job, file is erased."
else:
	print "Not quite, try again."
	exit(0)

print "Let's make sure by doing a cat on the file again."
print "Give this command: cat 'test.txt'"

prompt = str(raw_input(">>>"))

if prompt == "cat 'test.txt'":
	print ""
	print "See, the file is empty."
else:
	print "Not quite, try again."
	exit(0)

print "But that's no fun, let's put stuff back."
print "'target' is still a variable that points to the file."
print "Let's use that pointer to write back to the file."

print "Give this command: target.write('You can never replace what was gone.')"

prompt = str(raw_input(">>>"))

if prompt == "target.write('You can never replace what was gone.')":
	print "Good job!"
else:
	print "Not quite, try again."
	exit(0)

print "Now let's cat the file again and see what's in it."
print "Give this command: cat 'test.txt'"

prompt = str(raw_input("$"))

if prompt == "cat 'test.txt'":
	print "You can never replace what was gone."
	print "Good job, one last thing..."
else:
	print "Not quite, try again."
	exit(0)

print "It's important to close files after you're done to save memory."
print "Give this command: target.close()"

prompt = str(raw_input(">>>"))

if prompt == "target.close()":
	print "File closed, all done."
else:
	print "Dang, so close."
	print "Try again."
	exit(0)

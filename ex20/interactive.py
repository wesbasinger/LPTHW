from sys import exit

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

print "Now, let's connect the idea of functions with files."
print "These functions have been defined for you."

print '''
def print_all(f):
	print f.read()

def rewind(f):
	print f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()
	# the comma prints both statments to the same line
'''

print "First, let's get a handle to the file we're working with."

print "Give this command: current_file = open(input_file)"

prompt = raw_input('>>> ')

if prompt == "current_file = open(input_file)":
	current_file = open(".file.txt")
	print "Okay, now let's do so functions on that file."
else:
	print "Not quite, try again."
	exit(0)

print "First, let's print the whole file:\n"
print "Give this command: print_all(current_file)"

prompt = raw_input('>>> ')

if prompt == "print_all(current_file)":
	print_all(current_file)
	print "Good job, you see how it did that?"
else:
	print "Not quite, try again."
	exit(0)

print "Now let's rewind, kind of like a tape - if you know what that is."
print "Give this command: rewind(current_file)"

prompt = raw_input('>>> ')

if prompt == "rewind(current_file)":
	rewind(current_file)
	print "Good job, behind the scenes, it went back the first line."
else:
	print "Not quite, try again."
	exit(0)

print "Let's print a line. Set current_line to 1."
print "Give this command: current_line = 1"

new_prompt = str(raw_input('>>> '))


if new_prompt == "current_line = 1":
	print "Good job."
	current_line = 1
else:
	print "Not quite, try again."
	exit(0)

print "Now give this command: print_a_line(current_line, current_file)"

prompt = raw_input('>>> ')

if prompt == "print_a_line(current_line, current_file)":
	print_a_line(current_line, current_file)
	print "Good, see how that worked?"
else:
	print "Not quite, try again."
	exit(0)

print "Okay, I hope you have the general idea of how that works."
print "Head over to practice.py for hands on work."

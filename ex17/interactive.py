from sys import exit

print "If you read the exercise and did it, you"
print "got more practice with file commands."
print "Specificially, you copied material from one"
print "file and wrote it to another."

print "Let's replicate that process."
print "Let's assume you have two files in your directory,"
print "one is named 'fin.txt' and the other 'fout.txt'"

print "First, give this command: fin = open('fin.txt')"

prompt = str(raw_input(">>>"))
if prompt == "fin = open('fin.txt')":
	print "Good job! File open."
else:
	print "Try again, not quite."
	exit(0)

print "Now let's read it."
print "Give this command: indata = fin.read()"

prompt = str(raw_input(">>>"))
if prompt == "indata = fin.read()":
	print "Good job!  File read."
else:
	print "Try again, not quite."
	exit(0)

print "Let's see what's in 'fin.txt'."
print "Give this command: print indata"
prompt = str(raw_input(">>>"))

if prompt == "print indata":
	print """
	Fishes have fins.
	"""
	print "Good job! Next, we'll transfer the data."
else:
	print "Not quite, try again."
	exit(0)

print "Now let's get a pointer to the write file."
print "Give this command: fout = open('fout.txt', 'w')"

prompt = str(raw_input(">>>"))

if prompt == "fout = open('fout.txt', 'w')":
	print "Good job, you got the pointer."
else:
	print "Not quite, try again."
	exit(0)

print "Last, let's copy the data over."
print "Give this command: fout.write(indata)"

prompt = str(raw_input(">>>"))

if prompt == "fout.write(indata)":
	print "File copied, good job."
else:
	print "Try again!"
	exit(0)

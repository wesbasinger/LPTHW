# For this exercise, you will be using another file
# in this directory, called lumberjack.txt.
# You should not modify the contents of this file in any way.

# First, get a handle to the file by opening it.

current_file = open('lumberjack.txt')

# Okay, now define a function similar to what you saw in
# exercise, where the whole file is printed.


def print_all(current_file):
	print current_file.read()


# Okay, now write a function that will rewind back

def rewind(current_file):
	current_file.seek(0)	

# Okay, now write a function that will allow me to 
# print just one line.

def print_line(current_file):
	print current_file.readline()

# These function calls are for testing, don't change these
print_all(current_file)
rewind(current_file)
print_line(current_file)
print_line(current_file)

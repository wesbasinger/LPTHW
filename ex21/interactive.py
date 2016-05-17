from sys import exit

def multiply_by_two(number):
	return number * 2

def subtract_by_10(number):
	return number - 10

def compare_a_greater_than_b(first_num, second_num):
	return first_num > second_num


print "So far, you've done only printing with function."
print "Actually, most of the time you will want your"
print "function to return something."
print "Instead of printing the value to the screen,"
print "you save the value to variable or pass it in"
print "somewhere else."

print "These functions have been defined already for you."
print '''
def multiply_by_two(number):
	return number * 2

def subtract_by_10(number):
	return number - 10

def compare_a_greater_than_b(first_num, second_num):
	return first_num > second_num
'''

print "Let's do some math with those."
print "Give this command: multiply_by_two(40)"

prompt = raw_input('>>> ')

if prompt == "multiply_by_two(40)":
	multiply_by_two(40)
	print "See, nothing was printed."
else:
	print "Not quite, try again."
	exit(0)

print "This time let's print the value."
print "Give this command: print multiply_by_two(40)"

prompt = raw_input('>>> ')

if prompt == "print multiply_by_two(40)":
	print multiply_by_two(40)
	print "See, that worked."
else:
	print "Not quite, try again."
	exit(0)

print "Let's do some more."
print "Give this command: compare_a_greater_than_b(5,5)"

prompt = raw_input('>>> ')

if prompt == "compare_a_greater_than_b(5,5)":
	compare_a_greater_than_b(5,5)
	print "See, nothing was printed."
else:
	print "Not quite, try again."
	exit(0)

print "This time let's save the value to a variable."
print "Give this command: result = compare_a_greater_than_b(5,5)"

prompt = raw_input('>>> ')

if prompt == "result = compare_a_greater_than_b(5,5)":
	result = compare_a_greater_than_b(5,5)
	print "Your value is stored in result."
	print "Now I will print 'result' for you."
	print result
else:
	print "Not quite, try again."
	exit(0)

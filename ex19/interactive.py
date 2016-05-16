from sys import exit

def peanut_butter_and_jelly(peanut_butter_count, jelly_count):
	print "You have %d peanut butters." % peanut_butter_count
	print "You have %d jellies." % jelly_count
	print "Man, that's enough for a party."



print '''Suppose the following function is defined for you.
def peanut_butter_and_jelly(peanut_butter_count, jelly_count):
	print "You have %d peanut butters." % peanut_butter_count
	print "You have %d jellies." % jelly_count
	print "Man, that's enough for a party."
'''
print "Call the function directly with this command:"
print "peanut_butter_and_jelly(20, 30)"

prompt = raw_input('>>> ')

if prompt == "peanut_butter_and_jelly(20, 30)":
	peanut_butter_and_jelly(20, 30)
else:
	print "Not quite, try again."
	exit(0)

print "OR, we can use variables from our script:"
print "Define two variables by giving these commands."
print "amount_of_peanut_butter = 10"

prompt = raw_input('>>> ')

if prompt == "amount_of_peanut_butter = 10":
	amount_of_peanut_butter = 10
	print "Variable declared successfully."
else:
	print "Not quite, try again."
	exit(0)

print "amount_of_jelly = 20"

prompt = raw_input('>>> ')

if prompt == "amount_of_jelly = 20":
	amount_of_jelly = 20
	print "Variable declared successfully."
else:
	print "Not quite, try again."
	exit(0)

print "Now call the function with this command:"
print "peanut_butter_and_jelly(amount_of_peanut_butter, amount_of_jelly)"

prompt = raw_input('>>> ')

if prompt == "peanut_butter_and_jelly(amount_of_peanut_butter, amount_of_jelly)":
	peanut_butter_and_jelly(amount_of_peanut_butter, amount_of_jelly)
	print "See how that worked?"
else:
	print "Not quite, try again."
	exit(0)	


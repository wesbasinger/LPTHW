print "First, let's review the meaning of each of these logical operators."
print "Look at the operator, think to yourself what it means and press any key"
print "to see the definition."

print "There will be a test :-)"

print "LOGICAL OPERATOR: and"

prompt = raw_input()

if prompt != None:
	print "and: implies that two conditions are simultaneouly true"

print "LOGICAL OPERATOR: or"

prompt = raw_input()

if prompt != None:
	print "or: implies that either of two OR both conditions are true"

print "LOGICAL OPERATOR: not"

prompt = raw_input()

if prompt != None:
	print "not: implies the opposite of whatever it is applied to"

print "LOGICAL OPERATOR: !="

prompt = raw_input()

if prompt != None:
	print "!=: stands for not equal"

print "LOGICAL OPERATOR: =="

prompt = raw_input()

if prompt != None:
	print "==: equality comparison"

print "LOGICAL OPERATOR: >="

prompt = raw_input()

if prompt != None:
	print ">=: greater than or equal to"

print "LOGICAL OPERATOR: <="

prompt = raw_input()

if prompt != None:
	print "<=: less than or equal to"

print "LOGICAL OPERATOR: True"

prompt = raw_input()

if prompt != None:
	print "True: true"

print "LOGICAL OPERATOR: False"

prompt = raw_input()

if prompt != None:
	print "False: false"

print '''
Answer this following question.  Which of the following
is the logical operator for greater than or equal to?
a >=
b <=
c not
'''

answer = raw_input("ANSWER: ")

if answer.lower() == "a":
	print "Good job!"
else:
	print "Nope."

print '''
Answer this following question.  Which of the following
is the logical operator that requires both conditions to
be true.
a and
b not
c or
'''

answer = raw_input("ANSWER: ")

if answer.lower() == "a":
	print "Good job!"
else:
	print "Not quite."

print '''
Answer this following question.  What is the correct form
of true in Python?
'''

answer = raw_input("ANSWER: ")

if answer == "True":
	print "Good job."
else:
	print "Remember, capitilzation matters in Python."

print "Assume the following declarations are made."

print "homes = 20"
print "rooms_in_a_home = 3"
print "people = 100"
print "average_people_to_a_home = people / homes"
print "total_rooms = homes * rooms_in_a_home"

print "What is the value of 'average_people_to_a_home'?"
prompt = int(raw_input(">>>"))

if prompt == 5:
	print "Good job!"
else:
	print "Try again!"
	print "What is the value of 'average_people_to_a_home'?"
	prompt = int(raw_input(">>>"))

print "What is the value of 'total_rooms'?"
prompt = int(raw_input(">>>"))

if prompt == 60:
	print "Good job!"
else:
	print "Try again!"
	print "What is the value of 'total_rooms'?"
	prompt = int(raw_input(">>>"))

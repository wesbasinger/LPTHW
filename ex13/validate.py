from sys import argv
import unittest

from practice import hello_from_the_other_side

first = argv[1]
second = argv[2]

try:
	hello_from_the_other_side(argv[1], argv[2])

except IndexError:
	print "You're not giving enough command line arguments!"

print "There is no automatic test runner on this one, so if you got here, you win."

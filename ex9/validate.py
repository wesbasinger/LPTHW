import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

whitespace = print_text.split('\n')

delim = []

for entry in whitespace:
    delim.append(entry.rstrip())

class TestCanWorkWithNewlines(unittest.TestCase):

    def test_can_print_fib_on_newlines(self):
		self.assertEqual(
			str(delim[0]), 
			"1"
		)
		self.assertEqual(
			str(delim[1]),
			"1"
		)
		self.assertEqual(
			str(delim[2]),
			"2"
		)
		self.assertEqual(
			str(delim[3]),
			"3"
		)
		self.assertEqual(
			str(delim[4]),
			"5"
		)
		self.assertEqual(
			str(delim[5]),
			"8"
		)
		self.assertEqual(
			str(delim[6]),
			"13"
		)
		self.assertEqual(
			str(delim[7]),
			"21"
		)
		self.assertEqual(
			str(delim[8]),
			"34"
		)

    def test_can_break_one_line_into_many(self):
		self.assertEqual(
			str(delim[9]),
			"Roses are red,"
		)
		self.assertEqual(
			str(delim[10]),
			"Violets are blue,"
		)
		self.assertEqual(
			str(delim[11]),
			"Coding is fun,"
		)
		self.assertEqual(
			str(delim[12]),
			"Maybe it is new."
		)


if __name__ == '__main__':
    unittest.main()   


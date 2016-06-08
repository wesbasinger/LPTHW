import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class CanDeclareSimpleFunctions(unittest.TestCase):
	def test_can_make_a_function_with_one_arg(self):
		self.assertEqual(
			delim[0].rstrip(),
			"Monty Python and the Holy Grail"
		)
	
	def test_can_make_a_function_print_second_arg(self):
		self.assertEqual(
			delim[1].rstrip(),
			"Python"
		)

	def test_can_make_function_with_no_args(self):
		self.assertEqual(
			delim[2].rstrip(),
			"Depends"
		)


if __name__ == '__main__':
    unittest.main()   


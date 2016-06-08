import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class CanCallSimpleFunctions(unittest.TestCase):
	def test_can_call_with_own_argument(self):
		self.assertEqual(
			delim[0].rstrip(),
			"2 limbs have been chopped off."
		)
	
	def test_can_call_function_with_variable(self):
		self.assertEqual(
			delim[1].rstrip(),
			"4 limbs have been chopped off."
		)

	def test_variable_equals_4(self):
		self.assertEqual(
			bloody_stumps,
			4
		)



if __name__ == '__main__':
    unittest.main()   


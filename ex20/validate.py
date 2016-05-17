import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class CanCallSimpleFunctionsWithFileOps(unittest.TestCase):
	def test_can_make_print_all_function(self):
		self.assertEqual(
			delim[0],
			"Leaping from tree to tree! As they"
		)
		self.assertEqual(
			delim[4],
			"The Larch!"
		)
		self.assertEqual(
			delim[12],
			"I sleep all night and I work all day."
		)
	
	def test_can_make_print_line_function(self):
		self.assertEqual(
			delim[13],
			"Leaping from tree to tree! As they"
		)

	def test_variable_is_a_file_object(self):
		self.assertIsInstance(
			current_file,
			file
		)



if __name__ == '__main__':
    unittest.main()   


import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class CanFixSyntaxErrors(unittest.TestCase):

	def test_can_get_to_the_first_line(self):
		self.assertEqual(
			delim[0],
			"Let's practice everything."
		)
		self.assertEqual(
			delim[20],
			"all"
		)

if __name__ == '__main__':
    unittest.main()   


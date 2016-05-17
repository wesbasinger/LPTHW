import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class CanCopyAndPaste(unittest.TestCase):

	def test_copied_and_pasted(self):
		self.assertEqual(
			delim[0],
			"Let's practice everything."
		)
		self.assertEqual(
			delim[3],
			"--------------"
		)
		self.assertEqual(
			delim[4],
			""
		)
		self.assertEqual(
			delim[7],
			"cannot discern "
		)
		self.assertEqual(
			delim[9],
			"nor comprehend passion from intuition"
		)
		self.assertEqual(
			delim[10],
			"and requires an explanation"
		)

if __name__ == '__main__':
    unittest.main()   


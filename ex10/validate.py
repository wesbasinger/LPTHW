import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class TestCanUseEscapeCharacters(unittest.TestCase):

    def test_can_escape_double_quote(self):
		self.assertEqual(
			str(delim[0].rstrip()), 
			"I am 6'2\" tall."
		)

    def test_can_escape_single_quote(self):
		self.assertEqual(
			str(delim[1].rstrip()),
			'I am 6\'2" tall.'
		)

    def test_can_escape_a_backslash(self):
		self.assertEqual(
			str(delim[2].rstrip()),
			"I'm \\ a \\ cat."
		)


if __name__ == '__main__':
    unittest.main()   


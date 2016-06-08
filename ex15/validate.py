import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class TestCanOpenFiles(unittest.TestCase):
	def test_can_make_a_file_pointer(self):
		self.assertIsInstance(
            txt,
            file
        )
	def test_can_read_file_contents(self):
		self.assertEqual(
			contents[0:3],
			'DON'
		)
	def test_can_print_file_to_screen(self):
		self.assertEqual(
			str(delim[41]),
			"P2: Cuz they're made of... wood?"
		)


if __name__ == '__main__':
    unittest.main()   


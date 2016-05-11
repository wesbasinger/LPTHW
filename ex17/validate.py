import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

b = open('bravo.txt')

content = b.read()

class TestCanOpenFiles(unittest.TestCase):

	def test_can_make_a_file_pointer_to_alpha(self):
		self.assertIsInstance(
			alpha,
			file
	)
	
	def test_can_make_a_file_pointer_to_bravo(self):
		self.assertIsInstance(
			bravo,
			file
		)

	def test_can_copy_file(self):
		self.assertEqual(
			content,
			'Ten four mother goose.\nCopy that, Rodger.\n')


if __name__ == '__main__':
    unittest.main()   


import unittest
import subprocess

from practice import *

blank_test = open('blank.txt')

blank_contents = blank_test.read()

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class TestCanOpenFiles(unittest.TestCase):
	def test_can_make_a_file_pointer_to_blank(self):
		self.assertIsInstance(
			blank,
			file
	)
	
	def test_can_make_a_file_pointer_to_antiblank(self):
		self.assertIsInstance(
			antiblank,
			file
		)

	def test_can_truncate_file(self):
		self.assertEqual(
			blank_contents,
			""
		)
	

    def test_can_write_to_file(self):
		self.assertEqual(
			delim[0],
			'Testing, testing, 123'
		)

	def test_can_write_own_line(self):
		self.assertNotEqual(
			delim[1],
			None
			
		)


if __name__ == '__main__':
    unittest.main()   


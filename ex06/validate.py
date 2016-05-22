import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class TestCanUseStringFormatting(unittest.TestCase):

    def test_can_cat_row_row_row_your_boat(self):
		self.assertEqual(
			str(delim[0].rstrip()), 
			"Row, row, row your boat Gently down the stream."
		)

    def test_can_cat_mary_had_a_little_lamb(self):
		self.assertEqual(
			main_char,
			"Mary"
		)
		self.assertEqual(
			space,
			" "
		)
		self.assertEqual(
			verb,
			"had"
		)
		self.assertEqual(
			indef_art,
			"a"
		)
		self.assertEqual(
			adjective,
			"little"
		)
		self.assertEqual(
			direct_object,
			"lamb"
		)
		self.assertEqual(
			str(delim[1].rstrip()),
			"Mary had a little lamb"
		)

    def test_can_cat_takes_1_to_know_one(self):
		self.assertEqual(
			one,
			"one"
		)
		self.assertEqual(
			one_digit,
			"1"
		)
		self.assertEqual(
			str(delim[2].rstrip()),
			"Takes 1 to know one."
		)


if __name__ == '__main__':
    unittest.main()   


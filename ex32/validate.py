import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class CanCreateListsAndRunForLoops(unittest.TestCase):
	def test_can_make_a_list_of_odds_to_15(self):
		self.assertEqual(
			odds_to_15,
			[1, 3, 5, 7, 9, 11, 13, 15]
		)
	def test_can_make_a_list_of_strings(self):
		self.assertIn(
			"red" or "Red",
			colors_of_flag
		)
		self.assertIn(
			"blue" or "Blue",
			colors_of_flag
		)
		self.assertIn(
			"white" or "White",
			colors_of_flag
		)
		self.assertEqual(
			len(colors_of_flag),
			3
		)
	def test_can_make_assorted_list(self):
		self.assertIsInstance(
			assorted[0],
			str
		)
		self.assertIsInstance(
			assorted[1],
			int
		)
		self.assertIsInstance(
			assorted[2],
			bool
		)
		self.assertEqual(
			len(assorted),
			3
		)
	def test_can_do_a_basic_loop(self):
		self.assertEqual(delim[0].rstrip(),"1")
		self.assertEqual(delim[1].rstrip(),"3")
		self.assertEqual(delim[2].rstrip(),"5")
		self.assertEqual(delim[3].rstrip(),"7")
		self.assertEqual(delim[4].rstrip(),"9")
		self.assertEqual(delim[5].rstrip(),"11")
		self.assertEqual(delim[6].rstrip(),"13")
		self.assertEqual(delim[7].rstrip(),"15")

	def test_can_do_a_simple_loop(self):
		self.assertEqual(delim[8][-1].rstrip(), ".")
		self.assertEqual(delim[9][-1].rstrip(), ".")
		self.assertEqual(delim[10][-1].rstrip(), ".")

	def test_can_fill_a_list_with_for_loop(self):
		self.assertEqual(
			twenties,
			[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
		)


if __name__ == '__main__':
    unittest.main()   

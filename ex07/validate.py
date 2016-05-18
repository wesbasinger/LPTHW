import unittest

from practice import *

class TestCanUseStringFormatting(unittest.TestCase):

    def test_can_Pounce_4_times(self):
		self.assertEqual(
			word,
			"Pounce"
		)
		self.assertEqual(
			combined,
			"PouncePouncePouncePounce"
		)

    def test_can_make_plain_line_sep(self):
		self.assertEqual(
			char,
			"="
		)
		self.assertEqual(
			num_times,
			17
		)
		self.assertEqual(
			line_sep,
			"================="
		)

    def test_can_make_fancy_lin_sep(self):
		self.assertEqual(
			pattern,
			"+-"
		)
		self.assertEqual(
			repeat,
			8
		)
		self.assertEqual(
			together,
			"+-+-+-+-+-+-+-+-"
		)


if __name__ == '__main__':
    unittest.main()   


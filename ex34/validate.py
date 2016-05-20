import unittest

from practice import *

class CanAccessListElementsByIndex(unittest.TestCase):

	def test_can_make_5_element_list_with_apple_in_pos_3(self):
		self.assertEqual(
			len(five_elements), 5
		)
		self.assertEqual(
			five_elements[3],
			"apple"
		)

	def test_can_make_a_list_with_certain_index(self):
		self.assertEqual(
			len(four_elements),
			4
		)
		self.assertEqual(
			four_elements[0],
			"beginning index"
		)

	def test_can_access_by_index(self):
		self.assertEqual(
			number_one_hit,
			"Thriller"
		)

if __name__ == '__main__':
    unittest.main()   

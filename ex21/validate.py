import unittest
from practice import returns_2, plus_two, square, concat, compare_greater_than

class TestFunctionReturnsSomething(unittest.TestCase):

	def test_returns_two(self):
		self.assertEqual(
			return_two(2),
			2
		)
		self.assertEqual(
			return_two(7),
			2
		)
		self.assertEqual(
			return_two("test"),
			2
		)
	def test_plus_two(self):
		self.assertEqual(
			plus_two(0),
			2
		)
		self.assertEqual(
			plus_two(-19),
			-17
		)
	def test_square(self):
		self.assertEqual(
			square(5),
			25
		)
		self.assertEqual(
			square(-10),
			100
		)
	def test_concat(self):
		self.assertEqual(
			concat("Hello", "World"),
			"HelloWorld"
		)
	def test_compare_greater_than(self):
		self.assertEqual(
			compare_greater_than(9, 2),
			True
		)
		self.assertEqual(
			compare_greater_than(3,3),
			False
		)

if __name__ == '__main__':
    unittest.main()

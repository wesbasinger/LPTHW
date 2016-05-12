import unittest

from practice import one_time, one_of_two, dependable

monty = one_time("Monty Python and the Holy Grail")
monty_and_python  = one_of_two("Monty", "Python")
depends = dependable()

class TestIntroToFunctions(unittest.TestCase):

	def test_can_def_a_function_with_one_parameter(self):
		self.assertEqual(
			monty, 
			"Monty Python and the Holy Grail"
		)
	def test_can_def_a_function_that_only_prints_one_arg(self):
		self.assertEqual(
			monty_and_python,
			"Python"
		)
	def test_can_def_a_function_wo_parameters(self):
		self.assertEqual(
			depends,
			dependable
		)


if __name__ == '__main__':
    unittest.main()

import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class TestCanUseMathOperators(unittest.TestCase):

    def test_can_declare_capital_of_texas(self):
		self.assertEqual(
			capital_city_of_Texas,
			"Austin"
		)
        self.assertEqual(
			str(delim[0]), 
			"The capital of Texas is Austin."
		)

    def test_can_declare_num_sides_square(self):
		self.assertEqual(
			num_sides_of_a_square,
			4
		)
        self.assertEqual(
			str(delim[1]),
			"The number of sides in a square is 4."
		)

    def test_can_declare_a_boolean(self):
		self.assertEqual(
			water_is_a_molecule,
			True
		)
        self.assertEqual(
			str(delim[2]),
			"Is water a molecule? True"
		)

    def test_can_declare_num_sides_triangle(self):
		self.assertEqual(
			num_sides_of_a_triangle,
			3
		)
        self.assertEqual(
			str(delim[3]), 
			"A triangle has 1 less side than a square."
		)

    def test_can_declare_a_string_variable(self):
		self.assertEqual(
			marys_pet,
			"lamb"
		)
        self.assertEqual(
			str(delim[4]), 
			"Mary's pet was a little lamb."
		)


if __name__ == '__main__':
    unittest.main()                   

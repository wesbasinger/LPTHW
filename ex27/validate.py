import unittest
from practice import *

class TestBooleanSkills(unittest.TestCase):

	def test_not_boolean_skills(self):
		self.assertEqual(not_table_row_1, False)
		self.assertEqual(not_table_row_2, True)

	def test_or_boolean_skills(self):
		self.assertEqual(or_table_row_1, True)
		self.assertEqual(or_table_row_2, True)
		self.assertEqual(or_table_row_3, True)
		self.assertEqual(or_table_row_4, False)

	def test_and_boolean_skills(self):
		self.assertEqual(and_table_row_1, False)
		self.assertEqual(and_table_row_2, True)
		self.assertEqual(and_table_row_3, False)
		self.assertEqual(and_table_row_4, False)

	def test_nor_boolean_skills(self):
		self.assertEqual(nor_table_row_1, False)
		self.assertEqual(nor_table_row_2, False)
		self.assertEqual(nor_table_row_3, False)
		self.assertEqual(nor_table_row_4, True)

	def test_nand_boolean_skills(self):
		self.assertEqual(nand_table_row_1, True)
		self.assertEqual(nand_table_row_2, False)
		self.assertEqual(nand_table_row_3, True)
		self.assertEqual(nand_table_row_4, True)

	def test_not_equal_boolean_skills(self):
		self.assertEqual(not_equal_row_1, True)		
	



if __name__ == '__main__':
    unittest.main()

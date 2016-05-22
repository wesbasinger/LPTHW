import unittest

from practice import *

class CanCreateClassesAndMethods(unittest.TestCase):

	def test_can_finsh_a_class(self):
		test_dog = Dog("test_dog")
		self.assertEqual(test_dog.name, "test_dog")
		self.assertEqual(test_dog.bark(), "Ruff, ruff!")
		student = Student("test")
		self.assertEqual(student.name, "test")
		self.assertEqual(student.sleep(), "Sleeping...")

	def test_can_instantiate_objects(self):
		self.assertIsInstance(rex, Dog)
		self.assertIsInstance(mike, Student)

if __name__ == '__main__':
    unittest.main()   

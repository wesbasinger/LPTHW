import unittest

from practice import *

class CanUsePopAndJoinMethods(unittest.TestCase):

	def test_can_create_a_dictionary(self):
		self.assertEqual(
			grass,
			{
				"length" : 5,
				"is_noun" : True,
				"is_verb" : False,
				"vowels" : ["a"]
			}
		)
		self.assertEqual(
			truncate,
			{
				"length" : 8,
				"is_noun" : False,
				"is_verb": True,
				"vowels" : ['u', 'a', 'e']
			}
		)

	def test_can_access_dict_elements(self):
		self.assertEqual(
			soft,
			"feathers"
		)
		self.assertEqual(
			fuzzy,
			"short fur"
		)

if __name__ == '__main__':
    unittest.main()   

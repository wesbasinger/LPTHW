import unittest

from practice import *

class CanUsePopAndJoinMethods(unittest.TestCase):

	def test_can_split_a_string_into_a_list_and_pop(self):
		self.assertEqual(
			delim,
			[
				"I", 
				"only", 
				"regret", 
				"that", 
				"I", 
				"have",
				"but",
				"one",
				"life"
			]
		)

	def test_can_use_join(self):
		self.assertEqual(
			joined,
			"I~only~regret~that~I~have~but~one~life"
		)

if __name__ == '__main__':
    unittest.main()   

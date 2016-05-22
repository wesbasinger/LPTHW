import unittest

with open('practice.py') as p:
	for i, line in enumerate(p):
		if i == 15:
			ln16 = line
		elif i == 19:
			ln20 = line
		elif i == 22:
			ln23 = line
		elif i == 26:
			ln27 = line
		elif i == 32:
			ln33 = line
		elif i == 38:
			ln39 = line
		elif i == 41:
			ln42 = line
		elif i == 45:
			ln46 = line
		elif i == 49:
			ln50 = line
		elif i == 54:
			ln55 = line
		elif i == 57:
			ln58 = line
		elif i == 60:
			ln61 = line
		elif i == 63:
			ln64 = line
		elif i == 66:
			ln67 = line
		elif i == 69:
			ln70 = line
		elif i == 72:
			ln73 = line
		elif i == 75:
			ln76 = line
		elif i == 78:
			ln79 = line

class TestKnowsDiffBetweenHasAAndIsA(unittest.TestCase):

	def test_ln16(self):
		self.assertEqual(
			ln16.strip('\n').lower(),
			"## cat is-a animal"
			)

	def test_ln23(self):
		self.assertEqual(
			ln23.strip('\n').lower(),
			"## person is-a object"
			)


	def test_ln27(self):
		self.assertEqual(
			ln27.strip('\n').lower(),
			"## person has-a name of some kind"
			)


	def test_ln33(self):
		self.assertEqual(
			ln33.strip('\n').lower(),
			"## employee is-a person"
			)


	def test_ln39(self):
		self.assertEqual(
			ln39.strip('\n').lower(),
			"## employee has-a salary of some kind"
			)


	def test_ln42(self):
		self.assertEqual(
			ln42.strip('\n').lower(),
			"## fish is-a object"
			)


	def test_ln46(self):
		self.assertEqual(
			ln46.strip('\n').lower(),
			"## salmon is-a fish"
			)


	def test_ln50(self):
		self.assertEqual(
			ln50.strip('\n').lower(),
			"## halibut is-a fish"
			)


	def test_ln55(self):
		self.assertEqual(
			ln55.strip('\n').lower(),
			"## rover is-a dog"
			)


	def test_ln58(self):
		self.assertEqual(
			ln58.strip('\n').lower(),
			"## satan is-a cat"
			)


	def test_ln61(self):
		self.assertEqual(
			ln61.strip('\n').lower(),
			"## mary is-a person"
			)


	def test_ln64(self):
		self.assertEqual(
			ln64.strip('\n').lower(),
			"## mary has-a pet satan"
			)


	def test_ln67(self):
		self.assertEqual(
			ln67.strip('\n').lower(),
			"## frank is-a employee with name frank and salary 120000"
			)


	def test_ln70(self):
		self.assertEqual(
			ln70.strip('\n').lower(),
			"## frank has-a pet rover"
			)

	def test_ln73(self):
		self.assertEqual(
			ln73.strip('\n').lower(),
			"## flipper is-a fish"
			)


	def test_ln76(self):
		self.assertEqual(
			ln76.strip('\n').lower(),
			"## crouse is-a salmon"
			)


	def test_ln79(self):
		self.assertEqual(
			ln79.strip('\n').lower(),
			"## harry is-a halibut"
			)



if __name__ == '__main__':
    unittest.main()

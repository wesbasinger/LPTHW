import unittest

with open('practice.py') as p:
	for i, line in enumerate(p):
		if i == 15:
			line = ln16
		elif i == 19:
			line = ln20
		elif i == 22:
			line = ln23
		elif i == 26:
			line = ln27
		elif i == 32:
			line = ln33
		elif i == 38:
			line = ln39
		elif i == 41:
			line = ln42
		elif i == 45:
			line = ln46
		elif i == 49:
			line = ln50
		elif i == 57:
			line = ln58
		elif i == 60:
			line = ln61
		elif i == 63:
			line = ln64
		elif i == 66:
			line = ln67
		elif i == 69:
			line = ln70
		elif i == 72:
			line = ln73
		elif i == 75:
			line = ln76
		elif i == 78:
			line = ln79

class TestKnowsDiffBetweenHasAAndIsA(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()

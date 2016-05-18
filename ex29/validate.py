import unittest
import subprocess

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class CanTweakIfStatements(unittest.TestCase):
	def test_can_make_a_function_with_one_arg(self):
		self.assertEqual(
			delim[0],
			"For"
		)
		self.assertEqual(
			delim[1],
			"he's"
		)
		self.assertEqual(
			delim[2],
			"a"
		)
		self.assertEqual(
			delim[3],
			"jolly"
		)
		self.assertEqual(
			delim[4],
			"good"
		)
		self.assertEqual(
			delim[5],
			"fellow"
		)


if __name__ == '__main__':
    unittest.main()   


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
			delim[0].rstrip(),
			"For"
		)
		self.assertEqual(
			delim[1].rstrip(),
			"he's"
		)
		self.assertEqual(
			delim[2].rstrip(),
			"a"
		)
		self.assertEqual(
			delim[3].rstrip(),
			"jolly"
		)
		self.assertEqual(
			delim[4].rstrip(),
			"good"
		)
		self.assertEqual(
			delim[5].rstrip(),
			"fellow"
		)


if __name__ == '__main__':
    unittest.main()   


import unittest
import subprocess

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class CanTweakBooleanStatments(unittest.TestCase):
	def test_can_make_a_function_with_one_arg(self):
		self.assertEqual(
			delim[0],
			"True"
		)
		self.assertEqual(
			delim[1],
			"True"
		)
		self.assertEqual(
			delim[2],
			"True"
		)
		self.assertEqual(
			delim[3],
			"True"
		)
		self.assertEqual(
			delim[4],
			"True"
		)
		self.assertEqual(
			delim[5],
			"True"
		)


if __name__ == '__main__':
    unittest.main()   


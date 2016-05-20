import unittest
import subprocess

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class CanCreateWhileLoops(unittest.TestCase):

	def test_can_use_while_loop_to_print_to_5(self):
		self.assertEqual(delim[0], "1")
		self.assertEqual(delim[1], "2")
		self.assertEqual(delim[2], "3")
		self.assertEqual(delim[3], "4")
		self.assertEqual(delim[4], "5")

	def test_can_use_while_loop_to_populate_list(self):
		self.assertEqual(empty, [2, 4, 6, 8, 10])

if __name__ == '__main__':
    unittest.main()   
